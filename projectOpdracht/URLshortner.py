from flask import Flask, render_template, request, redirect
import hashlib
import sqlite3

def bereken_hash(data):
    hash = hashlib.sha256(data.encode())
    return hash.hexdigest()


def storeUrl(longUrl,hashUrl,shortUrl):
    con = sqlite3.connect("urls.db")
    cur = con.cursor()
    cur.execute(f"""
            INSERT INTO  urls (longUrl, urlHahs, shortUrl) VALUES
                ('{longUrl}','{hashUrl}','{shortUrl[10:16]}')
""")
    con.commit()
    con.close()



app = Flask(__name__)

@app.route('/',methods=["GET","POST"])
def URLshortner():
    if request.method == "POST":
        longUrl = request.form.get("url")
        hashUrl = bereken_hash(longUrl)
        shortUrl = f"localhost/{hashUrl[0:6]}"
        storeUrl(longUrl,hashUrl,shortUrl)
        return render_template('shortUrl.html',shortUrl=shortUrl)
    else:
        return render_template('URLform.html')

@app.route('/<shorUrl>')
def goToLongLink(shorUrl):
    print("hi")
    con = sqlite3.connect("urls.db")
    cur = con.cursor()
    cur.execute(f"SELECT longUrl FROM urls WHERE shortUrl = '{shorUrl}';")
    longLink = cur.fetchall()[0][0]
    con.close()
    return redirect(f"{longLink}")





if __name__ == '__main__':
    app.run(port=80)
