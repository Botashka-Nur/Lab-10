import psycopg2

def get_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="phonebook",
        user="postgres",
        password="Botashka07"
    )
    return conn
