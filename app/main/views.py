from flask import render_template, redirect, url_for
from . import main
from ..models import Asset
from .forms import AssetForm
from flask_login import login_required, current_user



@main.route('/')
@main.route('/home')
def index():
      
    return render_template('index.html')

@main.route('/assets/')
def assets():
    currentAssets = Asset.query.filter_by(category_id='Current Asset')
    financialAssets = Asset.query.filter_by(category_id='Financial Asset')
    fixedAssets = Asset.query.filter_by(category_id='Fixed Asset')
    
    return render_template('assets.html', currentAssets=currentAssets, financialAssets=financialAssets, fixedAssets=fixedAssets)

@main.route('/assets/new')
def assets_new():
    form = AssetForm()
    if form.validate_on_submit():
        description = form.description.data
        title = form.title.data
        category_id = form.category_id.data
        worth = form.worth.data
        new_asset = Asset(user_id=current_user.id, title = title,description=description,category_id=category_id, worth=worth)
        new_asset.save_asset()
        return redirect(url_for('main.assets'))
    return render_template('new_asset.html',form=form)
