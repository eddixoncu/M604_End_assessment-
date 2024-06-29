from flask import Blueprint, render_template,redirect, url_for, request
from website.forms import LoginForm,OwnerForm
from .controller import get_owner_by_document, get_vehicles, get_owners, update_owner
from .models import Owner

infractions = Blueprint ('infractions',__name__)

@infractions.route('/', methods=['GET','POST'])
def home():
    form = LoginForm()
    vehicles = get_vehicles()
    owners = get_owners()
    #for v in vehicles:
    #    print(f'{v.plate} :{v.brand}')
    return render_template('home.html', form=form, vehicles = vehicles, owners=owners)


@infractions.route('/owner/<int:id>',methods=['GET','POST'])
def owner(id):
    form= OwnerForm()
   
    if (request.method == "POST") :
        is_valid =form.validate_on_submit() #deber ser revisado
        print(f'valid is {is_valid}') 
        print(f'doc is {id}')
        print(f'name is {form.name.data}')
        print(f'last is {form.last_name.data}')
        #owner = Owner(document_number=id,names= form.name.data, last_names=form.last_name.data)
        #succes,reason = update_owner(owner)
    else:
        owner = get_owner_by_document(id)
        #print(f'names is {owner.names}')
        #form.name.data = owner.names
        #form.last_name.data = owner.last_names
        
   
    return render_template('owner.html',id=id, form=form)

    