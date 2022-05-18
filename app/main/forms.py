from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField, IntegerField
from wtforms.validators import Required


class AssetForm(FlaskForm):
    assetname = StringField('Asset Name', validators=[Required()])
    category_id = SelectField('Type of Assset', choices=[('currentAssets', 'Current Assets'), (
        'financialAssets', 'Financial Assets'), ('fixedAssets', 'Fixed Assets')])

    description = TextAreaField(
        'How best would you describe your Asset?', validators=[Required()])
    location = StringField('Asset Location', validators=[Required()])
    worth = IntegerField('Asset Value', validators=[Required()])

    submit = SubmitField('Submit')
