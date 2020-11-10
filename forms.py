from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class AnswerFormat(FlaskForm):
    First = StringField('Answer',
                           validators=[DataRequired()])
    Second = StringField('Answer',
                           validators=[DataRequired()])
    Third = StringField('Answer',
                           validators=[DataRequired()])
    Fourth = StringField('Answer',
                           validators=[DataRequired()])
    Fifth = StringField('Answer',
                           validators=[DataRequired()])
    Sixth = StringField('Answer',
                           validators=[DataRequired()])
    Seventh = StringField('Answer',
                           validators=[DataRequired()])
    Eighth = StringField('Answer',
                           validators=[DataRequired()])
    Ninth = StringField('Answer',
                           validators=[DataRequired()])
    Tenth = StringField('Answer',
                           validators=[DataRequired()])
    Eleventh = StringField('Answer',
                           validators=[DataRequired()])
    Twelfth = StringField('Answer',
                           validators=[DataRequired()])
    Thirteenth = StringField('Answer',
                           validators=[DataRequired()])


    submit = SubmitField('Sign Up')
