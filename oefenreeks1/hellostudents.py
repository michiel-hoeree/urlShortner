import sqlite3
from flask import Flask


con = sqlite3.connect("student.db")
cur = con.cursor()
cur.execute("SELECT * FROM Students")
rows = cur.fetchall()

app = Flask(__name__)

@app.route("/")
def studentList():
    list = "<ol>"
    for row in rows:
        list+=f"<li>{row}</li>"
    list+="</ol>"
    return list


    # <ol>
    #     <li>First Item</li>
    #     <li>Second Item</li>
    #     <li>Third Item</li>
    # </ol>