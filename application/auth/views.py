from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, login_required, current_user
from sqlalchemy.sql import text
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

    if Kayttaja.onko_olemassa(form.tunnus.data):
        return render_template("/auth/rekisteroitymislomake.html", form=form, error="Tunnus on jo käytössä")

    uusiKayttaja = Kayttaja(form.nimi.data, form.tunnus.data, form.salasana.data)

    db.session().add(uusiKayttaja)
    db.session().commit()

    login_user(uusiKayttaja)

    return redirect(url_for("tehtava_index"))




@app.route("/auth/hallinta", methods = ["GET"])
@login_required
def auth_hallinta():
    admin = "ADMIN" in current_user.roles()
    tehtavia_keskimaarin = Kayttaja.hae_tehtavien_keskiarvo()
    aihemaara = Kayttaja.hae_aiheiden_maara(current_user.id)
    return render_template("auth/hallinta.html", 
        admin=admin, tehtavia_keskimaarin=tehtavia_keskimaarin, aiheiden_maara=aihemaara)


@app.route("/auth/muuta_tietoja", methods = ["GET", "POST"])
@login_required
def muuta_tietoja():
    if request.method == "GET":
        return render_template("auth/muuta_tietoja.html", form = RekisteroitymisLomake())
    
    form = RekisteroitymisLomake(request.form)
    
    if not form.validate():
        return render_template("auth/muuta_tietoja.html", form = form)

    if form.tunnus.data != Kayttaja.query.filter_by(id=current_user.id).first().tunnus and Kayttaja.onko_olemassa(lomake.tunnus.data):
        return render_template("auth/muuta_tietoja.html", form = form, error = "Tunnus on jo käytössä")

    Kayttaja.muuta_tietoja(current_user.id, form.nimi.data, form.tunnus.data, form.salasana.data)
    
    return redirect(url_for("index"))
    

@app.route("/auth/poista_tili", methods = ["GET", "POST"])
@login_required
def poista_tili():
    if request.method == "GET":
        return render_template("auth/poista.html")

    nykyinen_id = current_user.id

    logout_user()

    Kayttaja.poista_tiedot(nykyinen_id)
    
    db.session.commit()

    return redirect(url_for("index"))



@app.route("/auth/uloskirjaudu")
def auth_uloskirjaudu():
    logout_user()
    return redirect(url_for("index"))
