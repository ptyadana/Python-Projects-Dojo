#from database.db, print out those countries with an area of greater than 2,000, 000.
#export results as csv

import sqlite3
import pandas as pd

conn = sqlite3.connect('database/database.db')
c = conn.cursor();

c.execute('SELECT * FROM countries WHERE area >= 2000000;')
results = c.fetchall();
conn.close();

df = pd.DataFrame.from_records(results);
df.columns = ['Rank', 'Country', 'Area', 'Population'];
df.to_csv('database/countries_with_big_area.csv');