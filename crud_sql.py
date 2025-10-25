import mysql.connector 
host="localhost",
port=3306,
user="root",
password="ilaki.kannan@04",
database="ilakiya"
# ------------------------------------------- 
def get_connection(): 
    try: 
        conn = mysql.connector.connect( 
             host="localhost",
             port=3306,
             user="root",
             password="ilaki.kannan@04",
             database="ilakiya"
         ) 
        return conn 
    except mysql.connector.Error as e: 
        print("Couldn't connect to MySQL. Please.") 
        print("Error:", e) 
        return None 
 
 
def create_student(): 
    name = input("Enter student name: ").strip() 
    age_text = input("Enter age (number): ").strip() 
    if not name or not age_text.isdigit(): 
        print("Please provide a name and a number for age.") 
        return 
    age = int(age_text) 
 
    conn = get_connection () 
 
    if not conn: return 
    cur = conn.cursor() 
    cur.execute("INSERT INTO students (name, age) VALUES (%s, %s)", (name, age)) 
    conn.commit() 
    print("Student added!") 
    cur.close() 
    conn.close() 
 
 
def read_students(): 
    conn = get_connection() 
    if not conn: return 
    cur = conn.cursor() 
    cur.execute("SELECT id, name, age FROM students ORDER BY id") 
    rows = cur.fetchall() 
    if not rows: 
        print("No students yet. Try option 1 to add one.") 
    else: 
        print("\n--- Students ---") 
        for row in rows: 
            print(f"ID: {row[0]} | Name: {row[1]} | Age: {row[2]}") 
    cur.close() 
    conn.close() 
 
def update_student(): 
    id_text = input("Enter the ID of the student to update: ").strip() 
    if not id_text.isdigit(): 
        print("Please enter a valid ID number.") 
        return 
    new_name = input("New name: ").strip() 
    new_age_text = input("New age (number): ").strip() 
    if not new_name or not new_age_text.isdigit(): 
        print("Please provide a name and a number for age.") 
        return 
    new_age = int(new_age_text) 
 
    conn = get_connection() 
    if not conn: return 
    cur = conn.cursor() 
    cur.execute("UPDATE students SET name=%s, age=%s WHERE id=%s", (new_name, new_age, id_text)) 
    conn.commit() 
    if cur.rowcount == 0: 
        print("No student with that ID was found.") 
    else: 
        print("Student updated!") 
    cur.close() 
    conn.close() 
 
def delete_student(): 
    id_text = input("Enter the ID of the student to delete: ").strip() 
    if not id_text.isdigit(): 
        print("Please enter a valid ID number.") 
        return 
 
    conn = get_connection() 
    if not conn: return 
    cur = conn.cursor() 
    cur.execute("DELETE FROM students WHERE id=%s", (id_text,)) 
    conn.commit() 
    if cur.rowcount == 0: 
        print("No student with that ID was found.") 
    else: 
        print("Student deleted!") 
    cur.close() 
    conn.close() 
 
def main(): 
    print("Python MySQL CRUD demo!\n") 
    while True: 
        print("Choose an option:") 
        print("1) Create (add a student)") 
        print("2) Read (show all students)") 
        print("3) Update (edit a student)") 
        print("4) Delete (remove a student)") 
        print("5) Exit") 
        choice = input("Your choice (1-5): ").strip() 
 
        if choice == "1": 
            create_student() 
        elif choice == "2": 
            read_students() 
        elif choice == "3": 
            update_student() 
        elif choice == "4": 
            delete_student() 
        elif choice == "5": 
            print("Goodbye!") 
            break 
        else: 
            print("Please choose 1, 2, 3, 4, or 5.\n") 
 
if __name__ == "__main__": 
    main() 