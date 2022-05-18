from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField, IntegerField
from wtforms.validators import Required


class AssetForm(FlaskForm):
    title = StringField('Title', validators=[Required()])
    category_id = SelectField('Asset', choices=[('currentAssets', 'Current Assets'), (
        'financialAssets', 'Financial Assets'), ('fixedAssets', 'Fixed Assets')])

    description = TextAreaField(
        'How best would you describe your Asset?', validators=[Required()])
    location = StringField('Asset Location', validators=[Required()])
    worth = IntegerField('Worth', validators=[Required()])

    submit = SubmitField('Submit')
