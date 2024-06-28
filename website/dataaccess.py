import sqlite3
from .models import Vehicle;

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