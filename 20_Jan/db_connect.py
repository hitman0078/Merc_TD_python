#Database connectivity with Postgres

import psycopg2

class EmployeeDAO:
    def __init__(self):
        self.conn=psycopg2.connect(host="localhost",
                      user="postgres",
                      password="postgres",
                      database="mbrdi",port=5432)
        self.cursor= self.conn.cursor()
        self.cursor.execute("create table employee(id int primary key,name varchar(40))")

    def add_employee(self,empid,name):
        self.cursor.execute("insert into employee values(%s,%s)",(empid,name))
        self.conn.commit()
    def display_employees(self):
        self.cursor.execute("select * from employee")
        rows= self.cursor.fetchall()
        for row in rows:
            print(row)
    def close_connection(self):
        self.conn.close()        

dao = EmployeeDAO()
dao.add_employee(101,'test')
dao.display_employees()            
