import time
from connection import cursor, db

def intro():
    print("=" * 80)
    print("{:^80s}".format("LIBRARY MANAGEMENT SYSTEM"))
    print("{:^80s}".format("PROJECT"))
    print("{:^80s}".format("MADE BY: SURYANSH"))
    print("=" * 80)
    print()
    time.sleep(2)
    
def create_record(): 
    id = int(input("\nBook ID: "))
    name = input("Book Name: ")
    author = input("Author Name: ")
    available = input("Available: ")
    sql = "INSERT INTO book(id,title,author,available) VALUES (%s,%s,%s,%s)"
    record = (id, name, author, available)
    cursor.execute(sql, record)
    db.commit()
    print("Record Entered Successfully\n")


def search(name):
    sql = "SELECT * FROM book WHERE TITLE = %s"
    value = (name,)
    cursor.execute(sql, value)
    record = cursor.fetchall()
    for i in record:
        if not record:
            print("\nNo such record exists")
            break
        else:
            print('\nBook ID: ', i[0])
            print('Book Name: ', i[1])
            print('Author Name: ', i[2])
            print('Available: ', i[3])

def display_all():
    cursor.execute("SELECT * FROM book")
    print('\n{0:20}{1:30}{2:15}{3:30}'.format('S.NO.', 'BOOK TITLE', 'BOOK AUTHOR', 'AVAILABLE'))
    for record in cursor:
        print('{0:20}{1:30}{2:15}{3:30}'.format(str(record[0]), record[1], record[2], record[3]))


def delete_record():
    display_all()
    try:
        id = int(input("Enter Book ID: "))
    except:
        print('Enter ID!')
        delete_record()
    sql = "DELETE FROM book WHERE ID = %s"
    value = (id,)
    cursor.execute(sql, value)
    db.commit()
    if cursor.rowcount == 0:
        print("\nBook not found!")
    else:
        print("\nRecord deleted successfully!")


def modify_record(id):
    sql = "SELECT * FROM book WHERE id = %s"
    value = (id,)
    cursor.execute(sql, value)
    record = cursor.fetchone()
    if not record:
        print("No such record exists")
    else:
        while True:
            print("\nEnter the option you want to change: ")
            print("1. ID")
            print("2. Title")
            print("3. Author")
            print("4. Availability")
            print("5. BACK")
            print()
            ch = int(input("Select Your Option (1-4): "))
            if ch == 1:
                new_id = input("Enter Book ID: ")
                sql = "UPDATE book SET ID = %s WHERE id = %s"
                values = (new_id, id)
                cursor.execute(sql, values)
                db.commit()
                print(cursor.rowcount, "record updated successfully")
            elif ch == 2:
                new_title = input("Enter Title of Book: ")
                sql = "UPDATE book SET title = %s WHERE id = %s"
                values = (new_title, id)
                cursor.execute(sql, values)
                db.commit()
                print(cursor.rowcount, "record updated successfully")
            elif ch == 3:
                new_author = input("Enter Name of Author : ")
                sql = "UPDATE book SET author = %s WHERE id = %s"
                values = (new_author, id)
                cursor.execute(sql, values)
                db.commit()
                print(cursor.rowcount, "record updated successfully")
            elif ch == 4:
                available = input("Available : ")
                sql = "UPDATE book SET available = %s WHERE id = %s"
                values = (available, id)
                cursor.execute(sql, values)
                db.commit()
                print(cursor.rowcount, "record updated successfully")
            elif ch == 5:
                break
            else:
                print("Invalid choice !!!\n")