from sqlite3 import connect
from data import tables
import pandas as pd 

def select(table_name):
    keys = tables[table_name]
    with connect('database.db') as con:
        cur = con.cursor()
        cmd = f"SELECT * FROM {table_name}"
        cur.execute(cmd)
        data = cur.fetchall()
        return data 

def insert(table_name, dict):
    keys = tables[table_name]['keys']
    values = [dict[key] for key in keys]
        
    with connect('database.db') as con: 
        cur = con.cursor()
        cmd = f"INSERT INTO {table_name} VALUES('" + "','".join(values) + "');"
        print(cmd   )
        cur.execute(cmd)
        con.commit()
    
def delete(table_name):
    with connect('database.db') as con:
        cur = con.cursor()
        cmd = f"DELETE FROM {table_name};"
        cur.execute(cmd)
        