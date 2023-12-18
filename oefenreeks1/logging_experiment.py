import sqlite3
from flask import Flask
import logging


app = Flask(__name__)           # Maakt de app zelf aan.
logging.basicConfig(filename='formData.log', encoding='utf-8', level=logging.DEBUG)     #gebruik loging in filename


@app.route("/greet")                 # route naar /greet
def studentList():
    list = "<ol>"                                   # word de list
    con = sqlite3.connect("student.db")             # verbind met de database student.db
    cur = con.cursor()                              # maak een cursor aan die in deze database staat
    cur.execute("SELECT * FROM Students")           # gebruik te cursor om alles te selecten
    rows = cur.fetchall()                           # fetch alle data geselect door de cursor
    for row in rows:
        list+=f"<li>{row}</li>"                     # verwerk rows naar de html list
    list+="</ol>"                                   # rond de list af
    app.logger.info('Visited the home page')        # infolog als deze pagina bezocht word
    app.logger.debug(list)                          # en list loggen als debug waneer deze pagina bezogt word
    return list                                     # zet list op de html pagina
