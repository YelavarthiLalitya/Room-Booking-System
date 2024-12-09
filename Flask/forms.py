from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField, DateField, TimeField
from wtforms.validators import DataRequired, Length, NumberRange, Optional, ValidationError  # Import ValidationError
from datetime import date

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=25)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=25)])
    submit = SubmitField('Login')

class CreateEventForm(FlaskForm):
    event_name = StringField('Event Name', validators=[DataRequired(), Length(max=100)])
    event_description = StringField('Event Description', validators=[DataRequired(), Length(max=200)])
    expected_attendance = IntegerField('Expected Attendance', validators=[DataRequired(), NumberRange(min=1)])
    event_date = StringField('Event Date (YYYY-MM-DD)', validators=[DataRequired()])
    start_time = StringField('Start Time (HH:MM)', validators=[DataRequired()])
    end_time = StringField('End Time (HH:MM)', validators=[DataRequired()])
    submit = SubmitField('Create Event')


    def validate_end_time(self, field):
        """Ensure end time is after start time."""
        if self.start_time.data and field.data and self.start_time.data >= field.data:
            raise ValidationError("End time must be after start time.")
