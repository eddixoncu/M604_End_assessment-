from flask import Blueprint, render_template
from website.forms import LoginForm
from .controller import get_vehicles, get_owners

infractions = Blueprint ('infractions',__name__)

@infractions.route('/', methods=['GET','POST'])
def home():
    form = LoginForm()
    vehicles = get_vehicles()
    owners = get_owners()
    for v in vehicles:
        print(f'{v.plate} :{v.brand}')
    return render_template('home.html', form=form, vehicles = vehicles, owners=owners)


@infractions.route('/owner/<int:id>',methods=['GET','POST'])
def owner(id):
    return render_template('owner.html',id=id)