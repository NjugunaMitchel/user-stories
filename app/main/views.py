from flask import render_template, request, redirect, url_for, flash
from . import main
from flask_login import login_required

@main.route('/')
@login_required
def index():
    title = 'hello world'
    return render_template('index.html', title = title)

 

