from .models import Owner
from .dataaccess import *

def get_vehicles():
    vehicles = []
    vehicles = get_vehicles_from_db()
    '''
    for i in range(0,10):
        v =Vehicle( plate=f'{i}-xx', brand='BRAND')
        vehicles.append(v)
    '''
    return vehicles

def get_owners():
    owners =[]
    owners = get_owners_from_db()
    return owners

def get_owner_by_document(document_number):
    owner = get_owner_by_document_db(document_number=document_number)
    return owner

def update_owner (owner:Owner):
    print(f'Calling update_owner from controller ')
    succes,reason = update_owner_db(owner)
    if not succes: print (reason)
    return succes,reason
