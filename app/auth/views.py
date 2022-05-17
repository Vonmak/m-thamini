from flask import render_template
from . import main


@main.route('/register')
def index():
      
      return render_template('register.html')