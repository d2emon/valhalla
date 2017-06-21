from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
# from wtforms.ext.sqlalchemy.fields import QuerySelectField


class HeroForm(FlaskForm):
    """
    Form for admin to add or edit a hero
    """
    name = StringField('Имя', validators=[DataRequired(), ])
    description = StringField('Описание', validators=[DataRequired(), ])
    submit = SubmitField('Подтвердить')
