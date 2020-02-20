from flask import redirect, render_template, request, url_for
from flask_login import current_user
from application.tehtava.models import Tehtava
from application.tehtava.forms import TehtavaLomake
from application.auth.models import Kayttaja
from application.aihe.models import Aihe, tehtavaAihe
from application import app, db, login_required
from sqlalchemy.sql import text

@app.route("/tehtava", methods=["GET"])
@login_required
def tehtava_index():

    tehtavalista = Kayttaja.hae_tehtavat(current_user.id)
    if len(tehtavalista) == 0:
        return render_template("tehtava/list.html")
    
    return render_template("tehtava/list.html", tehtavat=tehtavalista)

   # vanha tehtävälistaus
   # return render_template("tehtava/list.html", tehtavat = Tehtava.query.all())

@app.route("/tehtava/kaikki", methods=["GET"])
@login_required(role="ADMIN")
def tehtava_kaikki():

    stmt = text("SELECT tehtava.nimi, tehtava.kuvaus, tehtava.pvm, tehtava.valmis, tehtava.id"
                " FROM tehtava")
    
    tulos = db.engine.execute(stmt)

    tehtavalista = []
    for rivi in tulos:
        tehtavalista.append({"nimi":rivi[0], "kuvaus":rivi[1], "pvm":rivi[2], "valmis":rivi[3], 
                            "id":rivi[4]})
    if len(tehtavalista)==0: return render_template("tehtava/list.html")

    return render_template("tehtava/list.html", tehtavat=tehtavalista)


@app.route("/tehtava/uusi/")
@login_required(role="ANY")
def tehtava_lomake():
    return render_template("tehtava/uusi.html", form = TehtavaLomake())

@app.route("/tehtava/<tehtava_id>/", methods=["POST"])
@login_required
def tehtava_valmis(tehtava_id):

    tehtava = Tehtava.query.get(tehtava_id)
    tehtava.valmis = True
    db.session().commit()

    return redirect(url_for("tehtava_index"))

@app.route("/tehtava/", methods=["POST"])
@login_required(role="ANY")
def tehtava_luo():

    form = TehtavaLomake(request.form)

    if not form.validate():
        return render_template("tehtava/uusi.html", form = form)

    tehtava = Tehtava(request.form.get("nimi"))
    tehtava.valmis = form.valmis.data
    tehtava.kayttajaid = current_user.id
    tehtava.kuvaus = form.kuvaus.data
    tehtava.pvm = form.pvm.data
    aiheet = form.aihe.data.split(",")

    db.session().add(tehtava)
    db.session().commit()

    for aihe in aiheet:

        uusi_aihe = Aihe(aihe)

        db.session().add(uusi_aihe)
        db.session().commit()
        stmt = tehtavaAihe.insert().values(tehtavaid=tehtava.id, aiheid=uusi_aihe.id)

        db.session().execute(stmt)

    db.session().commit()

    return redirect(url_for("tehtava_index"))


@app.route("/tehtava/poista/<tehtava_id>")
@login_required(role="ADMIN")
def tehtava_poista(tehtava_id):

    tehtava = db.session.query(Tehtava).filter(Tehtava.id==tehtava_id).first()
    db.session.delete(tehtava)
    db.session().commit()

    return redirect(url_for("tehtava_index"))

@app.route("/tilastot/")
@login_required(role="ANY")
def tilastot_index():
    return render_template("/tehtava/tilastot.html")

@app.route("/tehtava/listaa_aiheet/", methods=["GET"])
@login_required(role="ANY")
def listaa_aiheet():
    aiheet = Kayttaja.hae_aiheet(current_user.id)
    return render_template("tehtava/listaa_aiheet.html", aiheet=aiheet)

@app.route("/tehtava/listaa_kayttajat/", methods=["GET"])
def listaa_kayttajat_joilla_tehtavia():
    tulos = Kayttaja.hae_kayttajat_joilla_tehtavia()

    return render_template("tehtava/listaa_kayttajat.html", kayttajat=tulos)

