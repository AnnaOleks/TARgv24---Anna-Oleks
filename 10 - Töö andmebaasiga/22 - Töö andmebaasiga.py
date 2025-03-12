from sqlite3 import *
from sqlite3 import Error

def create_connection(path):
    connection=None
    try:
        connection=connect(path)
        print("Uhendus on edukalt tehtud")
    except Error as e:
        print(f"Tekkis viga '{e}'")
    return connection

conn=create_connection("C:/Users/annao/source/repos/TARgv24 - Anna Oleks/AppData/data.db")

def execute_query(connection,query):
    try:
        cursor=connection.cursor()
        cursor.execute(query)
        connection.commit()
        print("Tabel on loodud")
    except Error as e:
        print(f"Viga'{e}' tabeli loomisega")

# create_users_table="""
# CREATE TABLE IF NOT EXISTS users(
# id INTEGER PRIMARY KEY AUTOINCREMENT,
# name TEXT NOT NULL,
# age INTEGER,
# gender TEXT,
# nationality TEXT
# );
# """

# execute_query(conn, create_users_table)

# create_users="""
# INSERT INTO
# users (name, age, gender, nationality)
# VALUES
# ('Mati', 25, 'mees', 'USA'),
# ('Lidia', 32, 'naine', 'France'),
# ('Mike', 40, 'mees', 'Denmark'),
# ('Elizabeth', 21, 'naine', 'Eesti');
# """

# execute_query(conn, create_users)

def execute_read_query(connection,query):
    cursor=connection.cursor()
    result=None
    try:
        cursor.execute(query)
        result=cursor.fetchall()
        return result
    except Error as e:
        print(f"Viga '{e}'")

# select_users="SELECT * from users"
# users=execute_read_query(conn, select_users)
# for user in users:
#     print(user)

# def add_users_query(connection, user_data):
#     query="INSERT INTO users(name,age,gender,nationality) VALUES("+user_data+")"
#     execute_query(connection,query)

# insert_user="'"+input("Nimi: ")+"','"+input("Vanus: ")+"','"+input("Sugu: ")+"','"+input("Riik:")+"'"

# add_users_query(conn,insert_user)

# elect_users="SELECT * from users"
# users=execute_read_query(conn, select_users)
# for user in users:
#     print(user)

def add_users_query_2(connection, user_data):
    """Lisame userit, mis on eraldi sisestatud"""
    query="INSERT INTO users(name, age, gender, nationality) VALUES(?,?,?,?)"
    cursor=connection.cursor()
    cursor.execute(query,user_data)
    connection.commit()

# insert_user=(input("Nimi: "), int(input("Vanus: ")), input("Sugu: "), input("Riik: "))
# print(insert_user)
# add_users_query_2(conn,insert_user)

# elect_users="SELECT * from users"
# users=execute_read_query(conn, select_users)
# for user in users:
#     print(user)

# def delete_data_from_tabel(connection,query):
#     try:
#         cursor=connection.cursor()
#         cursor.execute(query)
#         connection.commit()
#         print("Andmed on kustutatud")
#     except Error as e:
#         print(f"Viga'{e}' tabeli loomisega")

# print("Andmete kustutamine tabelist'users'")
# delete_data_from_userss="DELETE FROM users WHERE age<30"
# delete_data_from_tabel(conn,delete_data_from_userss)
# print("Tabelis 'uses' on jaanud need, kes on vanem kui 30: ")
# users=execute_read_query(conn, select_users)

# for user in users:
#     print(user)

# def delete_tabel(connection,query):
#     try:
#         cursor=connection.cursor()
#         cursor.execute(query)
#         connection.commit()
#         print("Tabel on kustutatud")
#     except Error as e:
#         print(f"Viga'{e}' tabeli loomisega")

# print("Tabeli kustutamine 'users'")
# delete_tabel_userss="DROP TABLE users"
# delete_tabel(conn,delete_tabel_userss)

create_gender_table="""
CREATE TABLE IF NOT EXISTS gender(
Id INTEGER PRIMARY KEY AUTOINCREMENT,
Nimetus TEXT NOT NULL)
"""

insert_gender="""
INSERT INTO
gender(nimetus)
VALUES
('mees'),
('naine')"""

create_users_table2="""
CREATE TABLE IF NOT EXISTS users2(
Id INTEGER PRIMARY KEY AUTOINCREMENT,
Name TEXT NOT NULL,
Lname TEXT NOT NULL,
Age INTEGER NOT NULL,
GenderId INTEGER,
FOREIGN KEY (GenderId) REFERENCES gender(Id)
)"""

insert_users2="""
INSERT INTO
users2(Name, Lname, Age, GenderId)
VALUES
('Mati','Tamm', 25, '1'),
('Lidia','Kask', 32, '2'),
('Mike','Tamm', 40, '1'),
('Elizabeth','Kuusk', 21, '2');
"""

select_users2="SELECT * FROM users2"
select_users2_gender="""
SELECT
users2.Name,
users2.Lname,
gender.Nimetus
from users2
INNER JOIN gender ON users2.GenderId=gender.Id
"""

execute_query(conn, create_gender_table)
execute_query(conn, insert_gender)

execute_query(conn, create_users_table2)
execute_query(conn, insert_users2)

users=execute_read_query(conn,select_users2)
print("kasutajate tabel 1,2:")
for user in users:
    print(user)

users_genders=execute_read_query(conn, select_users2_gender)
print("Kasutajate tabel mees, naine;")
for gender in users_genders:
    print(gender)