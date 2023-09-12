import psycopg2

def setupDB():
    connection = psycopg2.connect(database="postgres",
                               user="postgres",
                               password="pavan12345",
                               host="localhost",
                               port="5432")

    return connection