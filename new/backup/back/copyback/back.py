import mysql.connector
from mysql.connector import Error
import re

host='projarka-db'
user='user'
password='user'
db='projarka'

def create_con(host_name,user_name,password,database):
    connection=None
    try:
        connection=mysql.connector.connect(
                host=host_name,
                user=user_name,
                password=password,
                database=database,
		auth_plugin='mysql_native_password'
        )
        print("connect to DB successful")
    except Error as e:
        print(f"Error {e} happend")

        return connection

def exec_query(query):
    tr=mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=db
       )
    cursor=tr.cursor()
    result= None
    try:
        cursor.execute(query)
        result=cursor.fetchall()
        return result
    except Error as e:
        print(f"Error {e} in query")

test_query="""
select first_text
from first
"""


connect=create_con(host,user,password,db)
select= exec_query(test_query)
#print(f"result of first query is \n {select}")


pattern=r"([\w\s-]+!)"
text=re.search(pattern,str(select))


