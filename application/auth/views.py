from flask import render_template, request, redirect, url_for

from application import app
from application.auth.models import User
from application.templates.auth.forms import KirjautumisLomake

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/kirjautumislomake.html", form = LoginForm())


    form = KirjautumisLomake(request.form)
    # validoinnit



    kayttaja = Kayttaja.query.filter_by(kayttajanimi=form.kayttajanimi.data,
        salasana=form.salasana.data).first()

    if not kayttaja:
        return render_template("auth/kirjautumislomake.html",
            form = form, error = "No such username or password")

    print("Käyttäjä " + kayttaja.nimi + " tunnistettiin")
    return redirect(url_for("index"))
