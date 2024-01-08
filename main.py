from connection import db
from misc import intro, create_record, search, display_all, delete_record, modify_record

menu = '''\nMAIN MENU
1. DISPLAY ALL BOOKS
2. SEARCH BOOK
3. ADD BOOK
4. REMOVE BOOK
5. MODIFY BOOK DETAILS
6. QUIT\n\n'''

def main():
    intro()
    while True:
        print(menu)
        try:
            ch = int(input("Select Your Option (1-6): "))
        except:
            ch = 0
        if ch == 1:
            display_all()
        elif ch == 2:
            name = input("Enter Book Name: ")
            search(name)
        elif ch == 3:
            create_record()
        elif ch == 4:
            delete_record()
        elif ch == 5:
            display_all()
            id = input("Enter ID: ")
            modify_record(id)
        elif ch == 6:
            print("Thanks for using the software!")
            db.close()
            break
        else:
            print("Invalid choice")

# Code will only run if db is connected
if db.is_connected():
    main()
