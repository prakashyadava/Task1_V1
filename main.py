import csv
from allConn import *

file_path = 'int_clean_data.csv' // enter your csv file path
table_name = file_path[:-4]

def field_converstion():
    field = "("
    with open(file_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        header = csv_reader.fieldnames
        for i in range(len(header)-1):
            field = field + f'{header[i]},'
        field = field + f'{header[-1]})'
        return field
def create_table():
    temp = ""
    DBConnection.connect_db()
    with open(file_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        header = csv_reader.fieldnames
        for i in range(0,len(header)-1):
            temp = temp + f'{header[i]} varchar(100000),'
        temp = temp + f'{header[-1]} varchar(100000)'
        DBConnection.create_table(table_name,temp)
    DBConnection.close_db()

def insert_db():
    with open(file_path) as file:
        csvFile = csv.reader(file)
        csv_reader = csv.DictReader(file)
        header = csv_reader.fieldnames
        DBConnection.connect_db()
        count = 0
        field = field_converstion()
        for lines in csvFile:
            str_temp = ""
            for i in range(len(header)-1):
                line_temp = lines[i].replace("'","''")
                str_temp = str_temp + f"'{line_temp}'" + ','
            line_temp = lines[-1].replace("'","''")
            str_temp = str_temp + f"'{line_temp}'" 
            DBConnection.insert_data(table_name,field,str_temp)
            count = count +1
            print(count)
        DBConnection.close_db()
def read_data():
    DBConnection.connect_db()
    Log.log_read()
    data = DBConnection.display_records(table_name)
    DBConnection.close_db()
    print(data)

if __name__=='__main__':
    # create_table()
    # insert_db()
    # read_data()
    pass

