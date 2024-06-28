from .models import Vehicle
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