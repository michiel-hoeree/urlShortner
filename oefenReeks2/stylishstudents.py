from flask import Flask, render_template, url_for
import sqlite3
app = Flask(__name__)


@app.route("/")
def defname():
    con = sqlite3.connect("Students.db")
    cur = con.cursor()
    cur.execute(f"SELECT * FROM Students;")
    students = cur.fetchall()
    con.close()
    # url_for('static', filename='style.css')
    return render_template('jinjaHelloWorld.html', students=students)



if __name__ == '__main__':
    app.run()