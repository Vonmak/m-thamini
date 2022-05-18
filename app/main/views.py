from flask import render_template
from . import main


@main.route('/')
@main.route('/home')
def index():
      
      return render_template('index.html')
      

@main.route('/dashboard/index')
def user_dash():
      
      return render_template('dashboard/index.html')
