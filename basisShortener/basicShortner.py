from flask import Flask, request, redirect
import sqlite3


app = Flask(__name__)



def linkInDatabase(longLink,shortLink):
    con = sqlite3.connect("links.db")
    cur = con.cursor()
    cur.execute(f""" 
    INSERT INTO  links (longLink, shorLink) VALUES
        ('{longLink}','{shortLink}')
    """)
    con.commit()
    con.close()


@app.route('/',methods=["GET","POST"])
def default():
    if request.method == "POST":
        longLink = request.form.get("longLink")
        shortLink = request.form.get("shortLink")
        linkInDatabase(longLink,shortLink)
        return f"\"{longLink}\" word nu geredirect naar \"{shortLink}\"."
    return """
<form method="POST">
        <label for="longLink">longLink :</label>
        <input type="text" id="longLink" name="longLink" required><br>
        <label for="shortLink">shortLink :</label>
        <input type="text" id="shortLink" name="shortLink"><br>
        <input type="submit" value="Submit">
</form>"""

@app.route('/<shortLink>')
def goToLongLink(shortLink):
    con = sqlite3.connect("links.db")
    cur = con.cursor()
    cur.execute(f"SELECT longLink FROM links WHERE shorLink = '{shortLink}';")
    longLink = cur.fetchall()[0][0]
    con.close()
    return redirect(f"{longLink}")

if __name__ == '__main__':
    app.run()
