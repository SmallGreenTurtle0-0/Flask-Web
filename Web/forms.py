from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class EnterForm(FlaskForm):
    roomID = StringField(label="Room")
    date = StringField(label="Date")
    time = StringField(label="Time")
    submit = SubmitField(label='Submit')