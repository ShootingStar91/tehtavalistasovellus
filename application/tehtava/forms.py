from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, DateField, validators
from wtforms.widgets import TextArea

class TehtavaLomake(FlaskForm):
    nimi = StringField("Tehtävän nimi", [validators.Length(min=2)])
    valmis = BooleanField("Valmis")
    kuvaus = StringField("Kuvaus", widget=TextArea())
    pvm = DateField("Deadline", format='%d.%m.%Y', validators=(validators.Optional(),))
    aihe = StringField("Aihe")
    class Meta:
        csrf = False
