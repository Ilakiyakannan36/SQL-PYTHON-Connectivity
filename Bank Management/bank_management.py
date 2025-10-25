import json
import os
import mysql.connector

DATA_FILE = "bank_data.json"

# ---------------- JSON FUNCTIONS ---------------- #
def load_data():
    """Load account data from JSON file"""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}

def save_data(data):
    """Save account data to JSON file"""
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

# ---------------- SQL CONNECTION ---------------- #
def get_connection():
    """Connect to MySQL"""
    return mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="ilaki.kannan@04",
        database="bank"            
    )

# ---------------- CRUD OPERATIONS ---------------- #

# CREATE
def add_account(data):
    name = input("Enter account holder name: ").strip()
    if name in data:
        print(f"❌ Account for '{name}' already exists in JSON!")
        return data

    pin = input("Enter 4-digit PIN: ").strip()
    balance = float(input("Enter initial balance: "))

    data[name] = {
        "account_holder": name,
        "pin": pin,
        "balance": balance
    }

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO Accounts (account_holder, pin, balance)
        VALUES (%s, %s, %s)
    """, (name, pin, balance))
    conn.commit()
    conn.close()

    print(f"✅ Account for {name} added successfully!")
    return data


# READ
def read_accounts():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, account_holder, pin, balance, created_at FROM Accounts")
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        print("\nNo accounts found.")
    else:
        print("\n All Bank Accounts:")
        print("-" * 60)
        for row in rows:
            print(f"ID: {row[0]} | Name: {row[1]} | PIN: {row[2]} | Balance: ₹{row[3]:.2f} | Created: {row[4]}")
        print("-" * 60)


# UPDATE
def update_balance():
    name = input("Enter account holder name: ").strip()
    new_balance = float(input("Enter new balance: "))

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE Accounts SET balance=%s WHERE account_holder=%s", (new_balance, name))
    conn.commit()
    conn.close()

    if cursor.rowcount == 0:
        print("No account found with that name.")
    else:
        print(f"Balance updated successfully for {name}!")


# DELETE
def delete_account():
    name = input("Enter account holder name to delete: ").strip()

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Accounts WHERE account_holder=%s", (name,))
    conn.commit()
    conn.close()

    if cursor.rowcount == 0:
        print(" No account found with that name.")
    else:
        print(f" Account '{name}' deleted successfully!")


# ---------------- MAIN PROGRAM ---------------- #
def main():
    data = load_data()

    while True:
        print("\n---  BANK MANAGEMENT SYSTEM ---")
        print("1. Add Account")
        print("2. View Accounts")
        print("3. Update Balance")
        print("4. Delete Account")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            data = add_account(data)
            save_data(data)
        elif choice == "2":
            read_accounts()
        elif choice == "3":
            update_balance()
        elif choice == "4":
            delete_account()
        elif choice == "5":
            save_data(data)
            print(" Exiting...")
            break
        else:
            print("Invalid choice. Try again!")


if __name__ == "__main__":
    main()
