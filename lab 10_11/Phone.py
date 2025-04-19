import sqlite3
import csv

# Connect to SQLite database (creates it if it doesn't exist)
conn = sqlite3.connect("phonebook.db")
cursor = conn.cursor()

# Step 1: Create table
def create_table():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS PhoneBook (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        phone TEXT NOT NULL UNIQUE
    )
    """)
    conn.commit()

# Step 2.1: Insert from CSV
def insert_from_csv(filename="contacts.csv"):
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            try:
                name, phone = row
                cursor.execute("INSERT INTO PhoneBook (name, phone) VALUES (?, ?)", (name, phone))
            except Exception as e:
                print(f"Error inserting {row}: {e}")
    conn.commit()

# Step 2.2: Insert from console
def insert_from_console():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    try:
        cursor.execute("INSERT INTO PhoneBook (name, phone) VALUES (?, ?)", (name, phone))
        conn.commit()
        print("Contact added.")
    except Exception as e:
        print(f"Error: {e}")

# Step 3: Update data
def update_contact():
    phone = input("Enter the phone number of the contact to update: ")
    new_name = input("Enter new name (leave blank to skip): ")
    new_phone = input("Enter new phone (leave blank to skip): ")

    if new_name:
        cursor.execute("UPDATE PhoneBook SET name = ? WHERE phone = ?", (new_name, phone))
    if new_phone:
        cursor.execute("UPDATE PhoneBook SET phone = ? WHERE phone = ?", (new_phone, phone))

    conn.commit()
    print("Contact updated.")

# Step 4: Query data with filters
def query_contacts():
    print("1. All contacts")
    print("2. Filter by name")
    print("3. Filter by phone")
    choice = input("Choose filter option: ")
    if choice == "1":
        cursor.execute("SELECT * FROM PhoneBook")
    elif choice == "2":
        name = input("Enter name to search: ")
        cursor.execute("SELECT * FROM PhoneBook WHERE name LIKE ?", ('%' + name + '%',))
    elif choice == "3":
        phone = input("Enter phone to search: ")
        cursor.execute("SELECT * FROM PhoneBook WHERE phone LIKE ?", ('%' + phone + '%',))
    else:
        print("Invalid choice")
        return

    results = cursor.fetchall()
    for r in results:
        print(r)

# Step 5: Delete contact
def delete_contact():
    print("Delete by:")
    print("1. Name")
    print("2. Phone")
    choice = input("Choose option: ")
    if choice == "1":
        name = input("Enter name to delete: ")
        cursor.execute("DELETE FROM PhoneBook WHERE name = ?", (name,))
    elif choice == "2":
        phone = input("Enter phone to delete: ")
        cursor.execute("DELETE FROM PhoneBook WHERE phone = ?", (phone,))
    else:
        print("Invalid choice")
        return

    conn.commit()
    print("Contact(s) deleted.")

# Menu to test
def menu():
    create_table()
    while True:
        print("\n--- PhoneBook Menu ---")
        print("1. Insert from CSV")
        print("2. Insert manually")
        print("3. Update contact")
        print("4. Query contacts")
        print("5. Delete contact")
        print("6. Exit")

        choice = input("Enter choice: ")
        if choice == "1":
            insert_from_csv()
        elif choice == "2":
            insert_from_console()
        elif choice == "3":
            update_contact()
        elif choice == "4":
            query_contacts()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Try again.")

    conn.close()

if __name__ == "__main__":
    menu()
