from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, DateField, validators
from wtforms.widgets import TextArea

class TehtavaLomake(FlaskForm):
    nimi = StringField("Tehtävän nimi", [validators.Length(min=2), validators.Length(max=144)])
    valmis = BooleanField("Valmis")
    kuvaus = StringField("Kuvaus", [validators.Length(max=1000)], widget=TextArea())
    pvm = DateField("Deadline (dd.mm.yyyy)", format='%d.%m.%Y')
    aihe = StringField("Aiheet")
    class Meta:
        csrf = False
