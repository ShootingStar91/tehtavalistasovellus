from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, validators

class TehtavaLomake(FlaskForm):
    nimi = StringField("Tehtävän nimi", [validators.Length(min=2)])
    valmis = BooleanField("Valmis")

    class Meta:
        csrf = False
