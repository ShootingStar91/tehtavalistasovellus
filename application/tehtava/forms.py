from flask_wtf import FlaskForm
from wtforms import BooleanField, StringField, DateField, RadioField, validators
from wtforms.widgets import TextArea

class TehtavaLomake(FlaskForm):
    nimi = StringField("Tehtävän nimi", [validators.Length(min=2), validators.Length(max=144)])
    valmis = BooleanField("Valmis")
    kuvaus = StringField("Kuvaus", [validators.Length(max=1000)], widget=TextArea())
    pvm = DateField("Deadline (dd.mm.yyyy)", format='%d.%m.%Y', validators=[validators.Optional()])
    aihe = StringField("Aiheet")


    class Meta:
        csrf = False

class TehtavaHakuLomake(FlaskForm):
    alkupvm = DateField("Mistä alkaen (dd.mm.yyyy)", format='%d.%m.%Y')
    loppupvm = DateField("Mihin asti", format='%d.%m.%Y')
    valmis = RadioField("Valmis?", choices=[("kaikki", "Kaikki"), ("valmiit", "Valmiit"), ("kesken", "Tekemättömät")], default='kaikki')
    jarjestys = RadioField("Järjestys", choices=[("luomis", "Luomisajan mukaan"), ("nouseva", "Päivämäärän mukaan"), ("laskeva", "Käänteinen päivämääräjärjestys")], default='luomis')

    class Meta:
        csrf = False
