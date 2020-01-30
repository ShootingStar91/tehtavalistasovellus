from flaks_wtf import FlaskForm
from wtforms import PasswordField, StringField

class KirjautumisLomake(FlaskForm):
    tunnus = StringField("Tunnus")
    salasana = PasswordField("Salasana")

    class Meta:
        csrf = False
