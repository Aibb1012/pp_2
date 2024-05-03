# testt1
import psycopg2

conn = psycopg2.connect(host="localhost", dbname = "postgres", user = "postgres" , password = "18794" , port = 5432)
cur = conn.cursor()

conn.set_session(autocommit=True)
#do smth

cur.execute(""" CREATE TABLE IF NOT EXISTS person(
        id INT PRIMARY KEY,
        name VARCHAR(255),
        age INT,
        gender CHAR
);
""")
cur.execute(""" INSERT INTO person(id , name , age , gender) VALUES
(1 ,'Mike' , 30 , 'm'),
(2 , 'John' , 27 , 'm'),
(3 , 'Taika' , 34, 'f'),
(4 , 'Jenna' , 26 , 'f');

""")
