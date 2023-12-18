from flask import Flask
import sqlite3


# app = Flask(__name__)

con = sqlite3.connect("links.db")
cur = con.cursor()
cur.execute("CREATE TABLE links(longLink, shorLink)")
con.commit()
con.close()





# @app.route('/')
# def hello():
#     return 'Hello, Flask!'




# if __name__ == '__main__':
#     app.run()
