from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField,SelectField, IntegerField, PasswordField,BooleanField
from wtforms.validators import InputRequired ,Email,EqualTo
from wtforms import ValidationError

    

class AssetForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired()])
    description =TextAreaField('How best would you describe your Asset?', validators=[InputRequired()])
    worth = IntegerField('worth', validators=[InputRequired()])
    category_id = SelectField('Label', choices=[('currentAssets','Current Assets'),('financialAssets', 'Financial Assets'),('fixedAssets','Fixed Assets')])
    submit = SubmitField('Submit')


