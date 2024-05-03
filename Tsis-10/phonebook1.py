# phonebook1
#implement data from csv file
import psycopg2 , csv

# with open('sample.csv' , 'r') as file:
#     reader = csv.read(file)
#     # for x in re

conn = psycopg2.connect(host="localhost", dbname = "postgres", user = "postgres" , password = "18794" , port = 5432)
cur = conn.cursor()

conn.set_session(autocommit=True)
create_t = """
        CREATE TABLE IF NOT EXISTS phonebook (
            user_id SERIAL PRIMARY KEY,
            first_name VARCHAR(255) NOT NULL,
            last_name VARCHAR(255) NOT NULL,
            phone VARCHAR(255) UNIQUE NOT NULL
        );
        """
cur.execute(create_t)
print(''' Parameters
1 - search the contact by name
2 - search the contact by phone
3 - add a new contact
4 - add contact from .csv files
5 - change name or phone number of a contact
6 - delete by phonenumber
''')
num = int(input())

#do smth
if num ==1: #search by name
    name = input("Search by first name: ")
    
    cur.execute(
        "SELECT * FROM phonebook WHERE first_name = '{}'".format(name)
    )
    data = cur.fetchall()
    for x in data:
        print(x)

elif num ==2: #search by phone
    phone = input("Search by phone: ")
    cur.execute(
                "SELECT * FROM phonebook WHERE phone = '{}'".format(phone)
    )
    data = cur.fetchall()
    for x in data:
        print(x)

elif num ==3: #New contact
    first_name = input("Enter first name of user: ")
    last_name = input("Enter the last name of user: ")
    phone = input("Enter the user's phone num: ")
    
    cur.execute('''INSERT INTO phonebook (first_name, last_name, phone)
            VALUES (%s, %s, %s) ''' , ((first_name),(last_name), str(phone)))
    print("The new contact was created successfully")
    cur.execute("SELECT * FROM phonebook WHERE phone = '{}'".format(phone))
    data = cur.fetchall()
    for x in data:
        print(x)

elif num == 4:
    with open('sample.csv', 'r') as file:
        reader = csv.reader(file)

        next(reader)
        for x in reader:
            cur.execute('''INSERT INTO phonebook (first_name,last_name,phone) VALUES (%s, %s, %s)''', (x[0], x[1], x[2]))

elif num == 5:
    id = input("Enter the id of a contact: ")
    phone = input(f"Enter the new phone number: ")
    first_name = input(f"Enter the new first name: ")
    
    cur.execute('''UPDATE phonebook SET first_name = %s, phone = %s WHERE user_id = %s''' , (first_name , phone , id))
    print(f"Name and phone number of {id} has been changed")

elif num ==6:
    phone = input("Enter the phone number of the user: ")
    
    cur.execute(
        "DELETE FROM phonebook WHERE phone = '{}'".format(phone)
    )
    print(f"The contact with number {phone} has been removed")










