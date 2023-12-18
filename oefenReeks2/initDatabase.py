# from flask import Flask
import sqlite3


# app = Flask(__name__)

con = sqlite3.connect("Students.db")
cur = con.cursor()
cur.execute("CREATE TABLE Students(FirstName, LastName)")
cur.execute("""
            INSERT INTO  Students (FirstName, LastName) VALUES
                ('Michiel','Hoerée'),
                ('Inge','Yngvi'),
                ('Wesley','Trickz')
""")


con.commit()
con.close()





# @app.route('/')
# def hello():
#     return 'Hello, Flask!'




# if __name__ == '__main__':
#     app.run()
