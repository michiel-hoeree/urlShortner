import sqlite3
con = sqlite3.connect("Students.db")
cur = con.cursor()
cur.execute("CREATE TABLE Students(FirstName, LastName)")
cur.execute("""
            INSERT INTO  Students (FirstName, LastName) VALUES
                ('Michiel','Hoerée'),
                ('Inge','test'),
                ('Wesley','Trickz')
""")
con.commit()
con.close()

# con = sqlite3.connect("experiment.db")
# cur = con.cursor()
# # Query all rows from the Students table
# cur.execute("SELECT * FROM Students")
# rows = cur.fetchall()

# # Display the results
# for row in rows:
#     print(row)