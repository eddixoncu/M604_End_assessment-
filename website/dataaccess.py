import sqlite3
from .models import Vehicle, Owner;

_path='transit_registry.db'


def get_vehicles_from_db():
    try:
        vehicles = []
        with sqlite3.connect(_path ) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                           SELECT p.plate, b.brand 
                           from vehicles p
                           INNER JOIN  brands b on b.id=p.brand_id
                           limit 10""")
            output = cursor.fetchall()
            for row in output:
                v = Vehicle(plate=row[0],brand= row[1])
                vehicles.append(v)

        return vehicles


    except Exception as exc:
        print(f"ISSUE on get_all: {exc}")


def get_owners_from_db():
    try:
        people = []
        with sqlite3.connect(_path)as conn:
            cursor=conn.cursor();
            cursor.execute("""
                           SELECT  NUMERO_DOCUMENTO, NOMBRES, APELLIDOS
                           from  person
                           limit 10""")
            output = cursor.fetchall()
            for row in output:
                p = Owner(document_number=row[0],names=row[1],last_names=row[2])
                people.append(p)
        return people
    except Exception as exc:
        print(f"ISSUE on get_all: {exc}")

def get_owner_by_document_db(document_number):
    try:
        with sqlite3.connect(_path) as conn:
            print('consultado ower ', document_number)
            cursor = conn.cursor()
            sql = f'''
                  select  p.NUMERO_DOCUMENTO, p.NOMBRES, p.APELLIDOS FROM person p WHERE p.NUMERO_DOCUMENTO = '{document_number}' 
                   '''
            #args=(document_number)
            cursor.execute(sql)
            row = cursor.fetchone()
            if row:
                print('SI EXISTE OWNER')
                owner = Owner(document_number=row[0],names=row[1],last_names=row[2])
                return True,owner
            else:
                print('NO EXISTE OWNER')
                return False, "Owner not found"
            
    except Exception as exc:
        reason = f"ISSUE on get_owner_by_document_db: {exc}"
        print(reason)
        return False,reason
    
def update_owner_db(owner:Owner) :
    try:
        with sqlite3.connect(_path) as conn:
            cursor = conn.cursor()
            sql=""" UPDATE person SET nombres=?, apellidos=? WHERE numero_documento=? ;
                """
            args=(owner.names,owner.last_names, owner.document_number)
            cursor.execute(sql,args)
            return True, ""
    
    except Exception as exc:
        reason = f"ISSUE on get_all: {exc}"
        print(reason)
        return False,reason
