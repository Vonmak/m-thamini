from flask import render_template, redirect, url_for, flash
from . import main
from ..models import Asset, User
from .forms import AssetForm
from flask_login import login_required, current_user
from app import db


@main.route('/')
@main.route('/home')
def index():

    return render_template('index.html')


@main.route('/dashboard/index')
def user_dash():

    return render_template('dashboard/index.html')


@main.route('/assets/')
def asset():
    title = 'assets'
    assets = Asset.query.filter_by().first()
    currentAssets = Asset.query.filter_by(category_id='currentAssets')
    financialAssets = Asset.query.filter_by(category_id='financialAssets')
    fixedAssets = Asset.query.filter_by(category_id='fixedAssets')

    return render_template('assets.html', assets=assets, title=title, currentAssets=currentAssets, financialAssets=financialAssets, fixedAssets=fixedAssets)


@main.route('/assets/<int:user_id>/new', methods=['GET', 'POST'])
def assets_new(user_id):
    form = AssetForm()
    if form.validate_on_submit():
        description = form.description.data
        assetname = form.assetname.data
        category_id = form.category_id.data
        worth = form.worth.data
        location = form.location.data
        new_asset = Asset(user_id=user_id, assetname=assetname,
                          description=description, category_id=category_id, worth=worth, location=location)
        new_asset.save_assets()
        flash('Your asset has been added successfully', 'success')
        return redirect(url_for('main.asset', user_id=user_id))
    return render_template('new_asset.html', form=form)
