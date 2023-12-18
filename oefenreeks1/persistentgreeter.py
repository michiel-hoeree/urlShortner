import sqlite3
from flask import Flask, request, redirect
import logging


app = Flask(__name__)           # Maakt de app zelf aan.
logging.basicConfig(filename='formData.log', encoding='utf-8', level=logging.DEBUG)     #gebruik loging in filename


@app.route("/greet")                 # route naar /greet
def studentList():
    con = sqlite3.connect("formdata.db")             # verbind met de database formadata.db
    cur = con.cursor()                              # maak een cursor aan die in deze database staat
    cur.execute("SELECT * FROM Names")           # gebruik te cursor om alles te selecten
    rows = cur.fetchall()                           # fetch alle data geselect door de cursor
    voornaam = rows[-1][0]            # neem de laatste naam en toon de voornaam
    achternaam = rows[-1][1]           # neem de laatste naam ene too de achternaam

    html =f"Hallo, {voornaam} {achternaam}"         # maak de html
    app.logger.info('Visited the greet page')       # infolog als deze pagina bezocht word
    app.logger.debug(html)                          # en list loggen als debug waneer deze pagina bezogt word
    return html                                     # zet list op de html pagina

@app.route("/",methods=["GET","POST"])
def form():
    if request.method == "POST":                    # als we in deze route posten doe dit
        voornaam = request.form.get("voornaam")             #in de form staat een voornaam. onthoud deze
        achternaam = request.form.get("achternaam")         # in de form staat een achternaam. onthoud deze
        con = sqlite3.connect("formdata.db")
        cur = con.cursor()
        cur.execute(f"""
            INSERT INTO  Names (voornaam, achternaam) VALUES
                ('{voornaam}','{achternaam}')
""")
        con.commit()
        con.close()
        return redirect(f"/greet")      # ga naar deze link
    #als er geen post is stuur deze form waarmee gepost kan worden
    return """
<form method="POST">
        <label for="voornaam">voornaam :</label>
        <input type="text" id="voornaam" name="voornaam" required><br>
        <label for="achternaam">achternaam :</label>
        <input type="text" id="achternaam" name="achternaam"><br>
        <input type="submit" value="Submit">
</form>"""



# input gegegvens
# cur.execute("""
#             INSERT INTO  Students (FirstName, LastName) VALUES
#                 ('Michiel','Hoerée'),
#                 ('Inge','Yngvi'),
#                 ('Wesley','Trickz')
# """)