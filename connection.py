import mysql.connector

# connection to database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)

cursor = db.cursor()

if db.is_connected():
    print("\nSuccessfully Connected to MySQL Database\n")
    # creating database (if not exists)
    cursor.execute("create database if not exists library")
    cursor.execute("use library")
    # creating table (if not exist)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS book (
            ID int(100) PRIMARY KEY,
            TITLE char(80),
            AUTHOR char(40),
            AVAILABLE char(15)
        );
    """)
else:
    print("Not able to Connect MySQL Database!")
