#from database.db, print out those countries with an area of greater than 2,000, 000.

import sqlite3

conn = sqlite3.connect('database/database.db');
c = conn.cursor();

c.execute('SELECT * FROM countries WHERE area >= 2000000;');
results = c.fetchall();

for country in results:
    print(",".join(str(data) for data in country))

c.close();

