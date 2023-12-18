import sqlite3

# omdat een database meegeven aan digitap niet gaat (het maak de file te groot) kan dit script gebruikt worden om een database aan te maken.
# Er staan ook al een aantal dummy gegevens in om testing gemakelijker te maken

con = sqlite3.connect("urls.db")
cur = con.cursor()
cur.execute("CREATE TABLE urls(longUrl, urlHahs, shortUrl)")
cur.execute("""
            INSERT INTO  urls (longUrl, urlHahs, shortUrl) VALUES
                ('https://learning.ap.be/my/','e3294761e77f86e5514d8f6606cafe2f66b59c54bd641e112b256438cb728c9f','e3294'),
                ('https://www.youtube.com/','dbae2d0204aa489e234eb2f903a0127b17c712386428cab12b86c5f68aa75867','dbae2')
""")
con.commit()
con.close()
