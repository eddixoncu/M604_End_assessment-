from flask import Blueprint, render_template

infractions = Blueprint ('infractions',__name__)

@infractions.route('/', methods=['GET','POST'])
def home():

    return render_template('home.html')