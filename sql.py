import sqlite3 as lite
con=lite.connect('mtica.db')
cur=con.cursor()
cur.execute("DROP TABLE IF EXISTS Cars")
cur.execute(''' CREATE TABLE Cars(Id INT, Name TEXT, Price INT)''')
print('table Cars has created.')
cur.execute("INSERT INTO Cars VALUES(1,'audi',456123)")
cur.execute("INSERT INTO Cars VALUES(2,'TATA',456125)")
cur.execute("INSERT INTO Cars VALUES(3,'MG',456145)")
cur.execute("INSERT INTO Cars VALUES(4,'BENZ',456789)")
cur.execute("INSERT INTO Cars VALUES(5,'MAHINDRA',45641056)")
con.commit()
print("values in table Cars inserted")

