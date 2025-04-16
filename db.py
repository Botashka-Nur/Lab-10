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



"""from configparser import ConfigParser

def load_config(filename=r'C:\Users\Shaim\OneDrive\Рабочий стол\Python\Lab10\phonebook\database.ini', section='postgresql'):
    parser = ConfigParser()
    parser.read(filename)

    # get section, default to postgresql
    config = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            config[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return config

if __name__ == '__main__':
    config = load_config()
    print(config)"""