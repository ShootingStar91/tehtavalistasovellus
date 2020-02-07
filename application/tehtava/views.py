from application import app, db
from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user
from application.tehtava.models import Tehtava
from application.tehtava.forms import TehtavaLomake
from application.auth.models import Kayttaja
from application.aihe.models import Aihe
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

@app.route("/tehtava/uusi/")
@login_required
def tehtava_lomake():
    return render_template("tehtava/uusi.html", form = TehtavaLomake())

@app.route("/tehtava/<tehtava_id>/", methods=["POST"])
@login_required
def tehtava_valmis(tehtava_id):

    t = Tehtava.query.get(tehtava_id)
    t.valmis = True
    db.session().commit()

    return redirect(url_for("tehtava_index"))

@app.route("/tehtava/", methods=["POST"])
@login_required
def tehtava_luo():

    form = TehtavaLomake(request.form)

    if not form.validate():
        return render_template("tehtava/uusi.html", form = form)

    t = Tehtava(request.form.get("nimi"))
    t.valmis = form.valmis.data
    t.kayttajaid = current_user.id
    t.kuvaus = form.kuvaus.data
    aiheet = form.aihe.data.split(",")

    for aihe in aiheet:
        t.aiheet.append(Aihe(aihe))

    db.session().add(t)
    db.session().commit()

    return redirect(url_for("tehtava_index"))

@app.route("/tehtava/poista/<tehtava_id>")
@login_required
def tehtava_poista(tehtava_id):

    tehtava = db.session.query(Tehtava).filter(Tehtava.id==tehtava_id).first()
    db.session.delete(tehtava)
    db.session().commit()

    return redirect(url_for("tehtava_index"))

@app.route("/tilastot/")
@login_required
def tilastot_index():
    return render_template("/tehtava/tilastot.html")

@app.route("/tehtava/listaa_aiheet/", methods=["GET"])
@login_required
def listaa_aiheet():
    aiheet = Kayttaja.hae_aiheet(current_user.id)
    return render_template("tehtava/listaa_aiheet.html", aiheet=aiheet)
