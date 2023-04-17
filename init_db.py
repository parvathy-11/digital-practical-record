import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO details (username,password,user_type) VALUES (?,?, ?)",
            ('First username', 'Password of the first username','type of the user')
            )
cur.execute("INSERT INTO details (username,password,user_type) VALUES (?,?, ?)",
            ('Second username', 'Password of the second username','type of the user')
            )
cur.execute("INSERT INTO details (username,password,user_type) VALUES (?,?, ?)",
            ('Third username', 'Password of the third username','type of the user')
            )

            

connection.commit()
connection.close()