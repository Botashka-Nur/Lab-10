import psycopg2

def get_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="phonebook",
        user="postgres",
        password="Botashka07"
    )
    return conn

#SELECT * FROM user_score;
'''SELECT u.username, s.score, s.level, s.saved_at
FROM user_score s
JOIN users u ON u.id = s.user_id;'''
#SELECT * FROM users;

#SELECT * FROM contacts;
#SELECT * FROM phonebook;
#\dt
#SELECT username FROM phonebook;
#SELECT phone FROM phonebook;

