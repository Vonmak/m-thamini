from flask import render_template, redirect, url_for, flash, Flask, make_response, request
from . import main
from ..models import Asset, User, Subscriber
from .forms import AssetForm
from flask_login import login_required, current_user
from app import db, create_app
from ..email import mail_message
import pdfkit 

create_app = Flask(__name__)


@main.route('/report_<name>.pdf')
def report_pdf():
    # Make a PDF straight from HTML in a string.
    html = render_template('comments.html', name=name)
    pdf = pdfkit.from_string(html, False)
    response = make_response(pdf) 
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition']='inline; filename=output.pdf'  
    return  response



@main.route('/')
@main.route('/home')
def index():

    return render_template('index.html')


@main.route('/dashboard/index')
@login_required
def user_dash():

    return render_template('dash2.html')

@main.route('/assets/')
@login_required
def asset():
    title = 'assets'
    assets = Asset.query.filter_by().first()
    currentAssets = Asset.query.filter_by(category_id='currentAssets')
    financialAssets = Asset.query.filter_by(category_id='financialAssets')
    fixedAssets = Asset.query.filter_by(category_id='fixedAssets')

    return render_template('assets.html', assets=assets, title=title, currentAssets=currentAssets, financialAssets=financialAssets, fixedAssets=fixedAssets)


@main.route('/assets/<int:user_id>/new', methods=['GET', 'POST'])
@login_required
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
        return redirect(url_for('main.view', user_id=user_id))
    return render_template('new_asset.html', form=form)


@main.route('/tables')
@login_required
def view():
    posts = Asset.query.all()
    
    return render_template('tables.html', posts=posts)

@main.route("/location")
@login_required
def location():

    return render_template("locations.html")

@main.route('/subscribe',methods = ['POST','GET'])
def subscribe():
    email = request.form.get('subscriber')
    new_subscriber = Subscriber(email = email)
    new_subscriber.save_subscriber()
    mail_message("Subscribed to M-thamini","email/welcome_user",new_subscriber.email,new_subscriber=new_subscriber)
    flash('Successfully subscribed')
    return redirect(url_for('main.index'))