import psycopg2
import csv

def get_connection():
    conn = psycopg2.connect(
        dbname="phonebook",
        user="postgres",
        password="Botashka07",
        host="localhost",
        port="5432"
    )
    return conn

def create_table():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            username VARCHAR(255) NOT NULL,
            phone VARCHAR(20) NOT NULL
        );
    """)
    conn.commit()
    cur.close()
    conn.close()

def insert_from_csv(filename="contacts.csv"):
    conn = get_connection()
    cur = conn.cursor()
    try:
        with open(filename, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                cur.execute("INSERT INTO phonebook (username, phone) VALUES (%s, %s)", (row[0], row[1]))
        
        conn.commit()
        print(f" Data from {filename} file has been successfully added.")
    except FileNotFoundError:
        print(f"⚠ {filename} file not found.")
    finally:
        cur.close()
        conn.close()

def insert_from_console():
    conn = get_connection()
    cur = conn.cursor()
    username = input("Enter username: ")
    phone = input("Enter phone number: ")
    cur.execute("INSERT INTO phonebook (username, phone) VALUES (%s, %s)", (username, phone))
    conn.commit()
    print(f" Data for {username} has been successfully added.")
    cur.close()
    conn.close()

def update_data():
    conn = get_connection()
    cur = conn.cursor()

    print("Choose field to update:")
    print("1. Update username")
    print("2. Update phone number")

    choice = input("Choose method (1 or 2): ")

    if choice == '1':
        old_username = input("Enter old username: ")
        new_username = input("Enter new username: ")
        cur.execute("UPDATE phonebook SET username = %s WHERE username = %s", (new_username, old_username))
    elif choice == '2':
        username = input("Enter username: ")
        new_phone = input("Enter new phone number: ")
        cur.execute("UPDATE phonebook SET phone = %s WHERE username = %s", (new_phone, username))
    else:
        print(" Invalid choice!")
        return

    conn.commit()
    print("Data has been successfully updated.")
    cur.close()
    conn.close()

def query_data():
    conn = get_connection()
    cur = conn.cursor()

    print("Choose filter for querying data:")
    print("1. Query by username")
    print("2. Query by phone number")

    choice = input("Choose filter (1 or 2): ")

    if choice == '1':
        username = input("Enter username: ")
        cur.execute("SELECT * FROM phonebook WHERE username = %s", (username,))
    elif choice == '2':
        phone = input("Enter phone number: ")
        cur.execute("SELECT * FROM phonebook WHERE phone = %s", (phone,))
    else:
        print("⚠ Invalid choice!")
        return

    rows = cur.fetchall()
    if rows:
        for row in rows:
            print(f"Username: {row[1]}, Phone: {row[2]}")
    else:
        print("⚠ No data found.")
    
    cur.close()
    conn.close()

def delete_from_csv(username):
    with open('contacts.csv', mode='r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)

    rows = [row for row in rows if row[0] != username]

    with open('contacts.csv', mode='w', encoding='utf-8', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(rows)

def delete_data():
    conn = get_connection()
    cur = conn.cursor()

    print("Choose deletion method:")
    print("1. Delete by username")
    print("2. Delete by phone number")

    choice = input("Choose method (1 or 2): ")

    if choice == '1':
        username = input("Enter username: ")
        cur.execute("DELETE FROM phonebook WHERE username = %s", (username,))
        delete_from_csv(username)
    elif choice == '2':
        phone = input("Enter phone number: ")
        cur.execute("DELETE FROM phonebook WHERE phone = %s", (phone,))
        delete_from_csv(phone)
    else:
        print("Invalid choice!")
        return

    conn.commit()
    print("Data has been successfully deleted.")
    cur.close()
    conn.close()

def main():
    while True:
        print("\n PHONEBOOK MENU:")
        print("1. Insert data from CSV")
        print("2. Insert data manually")
        print("3. Update data")
        print("4. Query data")
        print("5. Delete data")
        print("6. Exit")

        choice = input("Your choice (1-6): ")

        if choice == '1':
            filename = input("Enter CSV filename: ")
            insert_from_csv(filename)
        elif choice == '2':
            insert_from_console()
        elif choice == '3':
            update_data()
        elif choice == '4':
            query_data()
        elif choice == '5':
            delete_data()
        elif choice == '6':
            print("Exiting Phonebook...")
            break
        else:
            print("Invalid choice! Please choose a valid option.")

if __name__ == "__main__":
    create_table()
    main()

