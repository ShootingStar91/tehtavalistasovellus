from application import app, db
from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user
from application.tehtava.models import Tehtava
from application.tehtava.forms import TehtavaLomake


@app.route("/tehtava", methods=["GET"])
def tehtava_index():
    return render_template("tehtava/list.html", tehtavat = Tehtava.query.all())

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

    db.session().add(t)
    db.session().commit()

    return redirect(url_for("tehtava_index"))
