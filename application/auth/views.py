from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user

from application import app
from application.auth.models import Kayttaja
from application.templates.auth.forms import KirjautumisLomake

@app.route("/auth/kirjaudu", methods = ["GET", "POST"])
def auth_kirjaudu():
    if request.method == "GET":
        return render_template("auth/kirjautumislomake.html", form = KirjautumisLomake())


    form = KirjautumisLomake(request.form)
    # validoinnit

    kayttaja = Kayttaja.query.filter_by(tunnus=form.tunnus.data,
        salasana=form.salasana.data).first()

    if not kayttaja:
        return render_template("auth/kirjautumislomake.html",
            form = form, error = "Ei löydetty tunnusta tai salasanaa")


    login_user(kayttaja)

    return redirect(url_for("index"))


@app.route("/auth/uloskirjaudu")
def auth_uloskirjaudu():
    logout_user()
    return redirect(url_for("index"))
