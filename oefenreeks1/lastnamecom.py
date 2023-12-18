from flask import Flask, redirect
import sqlite3



app = Flask(__name__)

# Define a route and a function to handle requests to that route
@app.route('/<voornaam>')
def goSomewhereElse(voornaam):
    con = sqlite3.connect("Students.db")
    cur = con.cursor()
    cur.execute(f"SELECT LastName FROM Students WHERE FirstName = '{voornaam}';")
    LastName = cur.fetchall()
    con.close()
    try:
        # return LastName[0][0]
        return redirect(f"https://www.{LastName[0][0]}.com/")
    except:
        return "een simpele 404 pagina"


# Run the Flask application
if __name__ == '__main__':
    app.run()