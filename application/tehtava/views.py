from application import app, db
from flask import redirect, render_template, request, url_for
from application.tehtava.models import Tehtava
from application.tehtava.forms import TehtavaLomake


@app.route("/tehtava", methods=["GET"])
def tehtava_index():
    return render_template("tehtava/list.html", tehtavat = Tehtava.query.all())

@app.route("/tehtava/uusi/")
def tehtava_lomake():
    return render_template("tehtava/uusi.html", form = TehtavaLomake())

@app.route("/tehtava/<tehtava_id>/", methods=["POST"])
def tehtava_valmis(tehtava_id):

    t = Tehtava.query.get(tehtava_id)
    t.valmis = True
    db.session().commit()

    return redirect(url_for("tehtava_index"))

@app.route("/tehtava/", methods=["POST"])
def tehtava_luo():
    t = Tehtava(request.form.get("nimi"))

    db.session().add(t)
    db.session().commit()

    return redirect(url_for("tehtava_index"))
