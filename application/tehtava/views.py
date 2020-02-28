from flask import redirect, render_template, request, url_for
from flask_login import current_user
from application.tehtava.models import Tehtava
from application.tehtava.forms import TehtavaLomake, TehtavaHakuLomake
from application.auth.models import Kayttaja
from application.aihe.models import Aihe, tehtavaAihe
from application import app, db, login_required
from sqlalchemy.sql import text, exists
import datetime

@app.route("/tehtava", methods=["GET", "POST"])
@login_required
def tehtava_index():
    form = TehtavaHakuLomake(request.form)

    if request.method == "GET":
        return render_template("tehtava/index.html", form=form, 
        vanhatAiheet=Kayttaja.hae_aiheet(current_user.id))

    valmius = form.valmis.data
    kysely = db.session().query(Tehtava).filter_by(kayttajaid=current_user.id)

    checkboxit = request.form.getlist("vanhaAihe")
    aiheet = []
    for checkbox in checkboxit:
        aiheet.append(int(checkbox))

    if valmius=='valmiit': kysely = kysely.filter_by(valmis=True)
    elif valmius=='kesken': kysely = kysely.filter_by(valmis=False)

    alkupvm, loppupvm = form.alkupvm.data, form.loppupvm.data
    if alkupvm == "" or alkupvm is None: alkupvm = datetime.date(1900, 1, 1)
    if loppupvm == "" or loppupvm is None: loppupvm = datetime.date(2999, 1, 1)
    loppupvm += datetime.timedelta(days=1)
    kysely = kysely.filter(Tehtava.pvm.between(alkupvm, loppupvm))

    if (form.jarjestys.data=='nouseva'): kysely = kysely.order_by(Tehtava.pvm)
    elif (form.jarjestys.data=='laskeva'): kysely = kysely.order_by(Tehtava.pvm.desc())

    if len(aiheet) > 0:
        kysely = kysely.join(Aihe, Tehtava.aiheet).filter(Aihe.id.in_(aiheet))

    tehtavalista = kysely.all()


    if len(tehtavalista) == 0:
        return render_template("tehtava/list.html")

    return render_template("tehtava/list.html", tehtavat=tehtavalista)


@app.route("/tehtava/kaikki", methods=["GET"])
@login_required(role="ADMIN")
def tehtava_kaikki():

    kysely = text("SELECT tehtava.nimi, tehtava.kuvaus, tehtava.pvm, tehtava.valmis, tehtava.id"
                " FROM tehtava")
    
    tulos = db.engine.execute(kysely)

    tehtavalista = []
    for rivi in tulos:
        tehtavalista.append({"nimi":rivi[0], "kuvaus":rivi[1], "pvm":str(rivi[2]), "valmis":rivi[3], 
                            "id":rivi[4]})

    if len(tehtavalista)==0: return render_template("tehtava/list.html")

    return render_template("tehtava/list.html", tehtavat=tehtavalista)


@app.route("/tehtava/uusi/")
@login_required(role="ANY")
def tehtava_lomake():
    vanhatAiheet = Kayttaja.hae_aiheet(current_user.id)
    return render_template("tehtava/uusi.html", form = TehtavaLomake(), vanhatAiheet = vanhatAiheet)

@app.route("/tehtava/<tehtava_id>/", methods=["POST"])
@login_required
def tehtava_valmis(tehtava_id):

    tehtava = Tehtava.query.get(tehtava_id)
    tehtava.valmis = True
    db.session().commit()

    return redirect(url_for("tehtava_index"))

@app.route("/tehtava/luo_uusi", methods=["POST"])
@login_required(role="ANY")
def tehtava_luo():

    form = TehtavaLomake(request.form)
    virheviesti = ""
    if not form.validate():
        virheviesti="Tarkista, että tehtävän nimessä on 2-144 merkkiä ja jos syötit päivämäärän, että se on oikeassa muodossa (esimerkiksi 1.2.2020 tai 05.04.2021 kelpaavat)"
        return render_template("tehtava/uusi.html", form=form, virheviesti=virheviesti, vanhatAiheet=Kayttaja.hae_aiheet(current_user.id))

    tehtava = Tehtava(request.form.get("nimi"))
    tehtava.valmis, tehtava.kayttajaid = form.valmis.data, current_user.id
    tehtava.kuvaus, tehtava.pvm = form.kuvaus.data, form.pvm.data

    if tehtava.pvm == None: tehtava.pvm = datetime.date.today()
    uudetAiheet = form.aihe.data.split(",")
    valitutAiheet = []
    vanhatAiheet = Kayttaja.hae_aiheet(current_user.id)

    checkboxit = request.form.getlist("vanhaAihe")
    for checkbox in checkboxit:
        valitutAiheet.append(Aihe.query.filter_by(id=int(checkbox)).first().nimi)
 
    for aihe in uudetAiheet:
        if aihe=="": continue
        valitutAiheet.append(aihe)

    db.session().add(tehtava)
    db.session().commit()

    for aihe in valitutAiheet:
        uusi_aihe_id = -1

        # Onko käyttäjän lisäämä aihe jo sittenkin olemassa?
        for vanhaAihe in vanhatAiheet:
            if aihe==vanhaAihe["nimi"]:
                uusi_aihe_id = vanhaAihe["id"]
                break

        if uusi_aihe_id==-1:
            uusi_aihe = Aihe(aihe)
            db.session().add(uusi_aihe)
            db.session().commit()
            uusi_aihe_id = uusi_aihe.id

        kysely = tehtavaAihe.insert().values(tehtavaid=tehtava.id, aiheid=uusi_aihe_id)
        db.session().execute(kysely)

    db.session().commit()

    return render_template("tehtava/uusi.html", form=TehtavaLomake(), vanhatAiheet = Kayttaja.hae_aiheet(current_user.id), viesti="Tehtävä lisätty sovellukseen!")


@app.route("/tehtava/poista/<tehtava_id>")
@login_required(role="ADMIN")
def tehtava_poista(tehtava_id):

    tehtava = db.session.query(Tehtava).filter(Tehtava.id==tehtava_id).first()
    db.session.delete(tehtava)
    db.session().commit()

    return redirect(url_for("tehtava_index"))
