from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField
from wtforms.validators import DataRequired

class UploadJD(FlaskForm):
	jd = TextAreaField(label = "Job Description", validators=[DataRequired()])
	submit = SubmitField(label = "Submit")
	