import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#from .models import Vehicle, Owner;

class Vehicle:
    def __init__(self, plate, brand) -> None:
        self.plate = plate
        self.brand = brand
        
class Owner:
    def __init__(self,document_number, names, last_names) -> None:
        self.document_number= document_number
        self.names =names
        self.last_names=last_names

class payment_chart:
    def __init__(self, yes, no)-> None:
        self.yes= yes
        self.no=no
    
    def to_dict(self):
        return {
            'yes': self.yes,
            'no': self.no,
        } 
    

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
        

def get_payment_status():
    try:
        payments = []
        with sqlite3.connect(_path)as conn:
            cursor=conn.cursor();
            cursor.execute("""
                           select IS_PAID, count (IS_PAID) as 'count' from infractions group by is_paid
                        """)
            output = cursor.fetchall()
            p=payment_chart(0,0)
            for row in output:
               
                if row[0]=='SI':
                    p=payment_chart(yes=row[1], no=0)
                else:
                    p=payment_chart(no=row[1],yes=0)
                   
                payments.append(p)
        
        return payments
    except Exception as exc:
        print(f"ISSUE on get_all: {exc}")


if __name__ == '__main__':
    print('hi')
    pays= get_payment_status()
    '''for p in pays:
        print(p.yes)
        print(p.no)
        
        
        In [87]: signals = [Signal(3, 9), Signal(4, 16)]

In [88]: pandas.DataFrame.from_records([s.to_dict() for s in signals])
Out[88]:
   x   y
0  3   9
1  4  16
        
    '''
    df=pd.DataFrame.from_records([s.to_dict() for s in pays])
    with pd.option_context('display.max_rows', None,
                       'display.max_columns', None,
                       'display.precision', 3,
                       ):
        #print(df)
        chart=df.sum().to_dict()
        colors=["green","yellow"]
        mylabels = chart.keys()
        values = chart.values()
        
        fig, ax = plt.subplots()
        ax.pie(values, labels=mylabels, autopct='%.0f%%',
            textprops={'size': 'smaller'}, radius=0.5, colors=colors)

        #plt.pie(values, labels=mylabels, colors=colors)
        ax.legend(title="Payment Distribution")
        plt.show()
       