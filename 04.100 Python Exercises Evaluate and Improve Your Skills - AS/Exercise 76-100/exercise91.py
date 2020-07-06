#read ten more countries from text file and add those too new_database.db
import sqlite3

conn = sqlite3.connect('database/database1.db')
c = conn.cursor();

# with open('database/ten_more_countries.txt', 'r') as file:
#     countries = file.read().splitlines();

# for country in countries[1:]:
#     info = country.strip().split(',');
#     c.execute("INSERT INTO countries VALUES(?, ?, ?, NULL)", (int(info[0]), info[1], int(info[2])));


# alternative way using pandas #
import pandas as pd;

df = pd.read_csv('database/ten_more_countries.txt');

for index, row in df.iterrows():
    c.execute("INSERT INTO countries VALUES(?, ?, ?, NULL)", (row['ID'], row['Country'], row['Area']));

conn.commit();
conn.close();