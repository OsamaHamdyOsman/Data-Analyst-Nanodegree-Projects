from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
from wtforms.validators import DataRequired


class Inputs(FlaskForm):
    cities = ['Chicago', 'New York City', 'Washington']
    city = SelectField('City', choices = cities, validators = [DataRequired()])

    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'All']
    month = SelectField('Month', choices = months, validators = [DataRequired()])

    days = ['Mon', 'Tues', 'Wedn', 'Thru', 'Fri', 'Sat', 'Sun', 'All']
    day = SelectField('Day', choices = days, validators = [DataRequired()])

    submit = SubmitField('Submit My Filters')



class RawData(FlaskForm):
    choices = ['Yes', 'No']
    display = SelectField('display', choices = choices, validators = [DataRequired()])

    submit = SubmitField('Submit My Filters')
