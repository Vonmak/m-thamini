from flask import render_template
from . import auth


@auth.route('/register')
def register():
      
      return render_template('register.html')


@auth.route('/login')
def login():
      
      return render_template('login.html')


@auth.route('dashboard/tables')
def tables():
      
      return render_template('dashboard/tables.html')


@auth.route('dashboard/add_assets')
def add_assets():
      
      return render_template('dashboard/add_assets.html')