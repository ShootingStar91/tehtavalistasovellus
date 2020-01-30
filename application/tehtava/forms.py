from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField

class TehtavaLomake(FlaskForm):
    nimi = StringField("Tehtävän nimi")
    valmis = BooleanField("Valmis")

    class Meta:
        csrf = False


