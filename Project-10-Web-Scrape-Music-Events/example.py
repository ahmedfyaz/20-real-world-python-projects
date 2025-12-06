import  sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

#Query data
cursor.execute("SELECT* FROM events WHERE date = '2088.10.14'")
rows = cursor.fetchall()
print(rows)

#Query Certain columns
cursor.execute("SELECT band FROM events WHERE date = '2088.10.14'")
rows = cursor.fetchall()
print(rows)

#Insert new rows
#
# new_rows = [('Cats','Cat City','2026.10.12'),
#             ('Dogs','Dog City','2026.10.12')]
#
# cursor.executemany("INSERT INTO events VALUES(?,?,?)",new_rows)
# connection.commit()

cursor.execute("SELECT* FROM events WHERE date = '2026.10.12'")
rows = cursor.fetchall()
print(rows)