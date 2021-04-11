from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class EnterForm(FlaskForm):
    ID = StringField(label="ID of 'phong thi'")
    submit = SubmitField(label='submit')