from flask_wtf import FlaskForm
from wtforms import StringField

class TehtavaLomake(FlaskForm):
    nimi = StringField("Tehtävän nimi")

    class Meta:
        csrf = False


