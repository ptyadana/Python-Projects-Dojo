import sqlite3

conn = sqlite3.connect('my_friends.db');
c = conn.cursor();

c.execute('CREATE TABLE friends(first_name TEXT, last_name TEXT, closeness INT)');

data = ('Perry', 'Kid', 7);
query = "INSERT INTO friends VALUES(?,?,?)";
c.execute(query, data);

people = [
    ('Jennifer', 'Al', 4),
    ('Daniel', 'Boom', 6),
    ('Cat', 'Zee', 2),
    ('James', 'Mid', 8),
]

c.executemany(query, people);

c.execute('SELECT * FROM friends;');

# Iterate over cursor
for result in c:
    print(result);

# fetch all the results
people_list = c.fetchall();
print(people_list);

# fetch only first one result
c.execute('SELECT * FROM friends WHERE first_name = "Perry";');
print(c.fetchone());

c.execute("SELECT * FROM friends WHERE closeness > 5");
print(c.fetchall());

conn.commit();
conn.close();