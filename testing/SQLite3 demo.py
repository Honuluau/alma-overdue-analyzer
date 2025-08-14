import sqlite3
# Following along with the https://docs.python.org/3/library/sqlite3.html tutorial.

con = sqlite3.connect("example/tutorial.db")
cur = con.cursor()

# cur.execute("CREATE TABLE movie(title, year, score)")

cur.execute("""
    INSERT INTO movie VALUES
        ('Monty Python and the Holy Grail', 1975, 8.2),
        ('And Now for Something Completely Different', 1971, 7.5)
""")

con.commit()