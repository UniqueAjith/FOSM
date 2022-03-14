import mysql.connector

__cnx = None

def get_sql_connection():
    print('mysql connection is Opening...')
    global __cnx
    if __cnx is None:
        __cnx = mysql.connector.connect(user='root', password='SQL@123',
                              host='127.0.0.1',
                              database='food_ordering')
    return __cnx