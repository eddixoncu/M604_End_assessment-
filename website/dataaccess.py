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