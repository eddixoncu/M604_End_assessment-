from flask import Blueprint, render_template
from website.forms import LoginForm
from .controller import get_vehicles

infractions = Blueprint ('infractions',__name__)

@infractions.route('/', methods=['GET','POST'])
def home():
    form = LoginForm()
    vehicles = get_vehicles()
    for v in vehicles:
        print(f'{v.plate} :{v.brand}')
    return render_template('home.html', form=form, vehicles = vehicles)