from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators

class KirjautumisLomake(FlaskForm):
    tunnus = StringField("Tunnus")
    salasana = PasswordField("Salasana")

    class Meta:
        csrf = False

class RekisteroitymisLomake(FlaskForm):
    nimi = StringField("Nimi", [validators.Length(min=3), validators.Length(max=144)])
    tunnus = StringField("Tunnus", [validators.Length(min=3), validators.Length(max=30)])
    salasana = PasswordField("Salasana", [validators.Length(min=4), validators.Length(max=30)])

    class Meta:
        csrf = False


