from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user

from application import app, db
from application.auth.models import Kayttaja
from application.auth.forms import KirjautumisLomake, RekisteroitymisLomake

@app.route("/auth/kirjaudu", methods = ["GET", "POST"])
def auth_kirjaudu():
    if request.method == "GET":
        return render_template("auth/kirjautumislomake.html", form = KirjautumisLomake())


    form = KirjautumisLomake(request.form)

    kayttaja = Kayttaja.query.filter_by(tunnus=form.tunnus.data,
        salasana=form.salasana.data).first()

    if not kayttaja:
        return render_template("auth/kirjautumislomake.html",
            form = form, error = "Ei löydetty tunnusta tai salasanaa")


    logout_user()
    login_user(kayttaja)
    return redirect(url_for("tehtava_index"))

@app.route("/auth/rekisteroidy", methods = ["GET", "POST"])
def auth_rekisteroidy():
    if request.method == "GET":
        return render_template("auth/rekisteroitymislomake.html", form = RekisteroitymisLomake())

    form = RekisteroitymisLomake(request.form)

    if not form.validate():
        return render_template("/auth/rekisteroitymislomake.html", form=form)

    uusiKayttaja = Kayttaja(form.nimi.data, form.tunnus.data, form.salasana.data)



    db.session().add(uusiKayttaja)
    db.session().commit()

    
    login_user(uusiKayttaja)

    return redirect(url_for("tehtava_index"))

@app.route("/auth/uloskirjaudu")
def auth_uloskirjaudu():
    logout_user()
    return redirect(url_for("index"))
