from log import *
from config import config
import psycopg2
class DBConnection:
    conn = None
    cur = None
    def __init__(self):
        pass
    @classmethod
    def connect_db(cls):
        params = config()
        cls.conn  = psycopg2.connect(**params)
        cls.cur = cls.conn.cursor()
        Log.log_connection(True)
    @classmethod
    def create_table(cls,name,table):
        cls.cur.execute(f"create table if not exists {name}(int serial primary key,{table}) ;")
        cls.conn.commit()
        Log.log_read()
    @classmethod
    def get_records(cls,name):
        try:
            cls.cur.execute(f"select * from {name} ;")
            data  =cls.cur.fetchall()
            return data
        except Exception as e:
            print(e)

    @classmethod
    def insert_data(cls,name,field,data):
        cls.cur.execute(f"insert into {name} {field} values ({data});")
        cls.conn.commit()
    @classmethod
    def close_db(cls):
        cls.conn.close()
        Log.log_close(True)
