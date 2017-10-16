import sqlite3

conn = sqlite3.connect('R_Gen.db')

c = conn.cursor()
c.execute("SELECT * FROM Ingredients WHERE Ingredient_ID=2")

print(c.fetchone())

conn.commit()
conn.close()
