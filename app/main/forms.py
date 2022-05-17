from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField,SelectField, IntegerField
from wtforms.validators import Required

    

class AssetForm(FlaskForm):
    title = StringField('Title', validators=[Required()])
    description =TextAreaField('How best would you describe your Asset?', validators=[Required()])
    worth = IntegerField('worth', validators=[Required()])
    category_id = SelectField('Label', choices=[('currentAssets','Current Assets'),('financialAssets', 'Financial Assets'),('fixedAssets','Fixed Assets')])
    submit = SubmitField('Submit')