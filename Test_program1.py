import sqlite3
conn = sqlite3.connect("emaildb.sqlite")
cur = conn.cursor()

cur.execute('CREATE TABLE Count1 (email TEXT,count INTEGER)')

fname=input('Enter filename : ')

fh = open(fname)
for line in fh:
    if line.startswith('From: '):
        continue
    pieces = line.split()
    email = pieces[1]
    cur.execute('SELECT count from Counts1 where email = ? ',(email,))
    row=cur.fetchone()
    if row is None:
        cur.execute('INSERT INTO Counts1(email,count) values(?,1)',(email,))
    else:
        cur.execute('UPDATE Counts1 SET count = count+1 where email = ? ',(email,))
    conn.commit()

sqlstr='Select email,count from COUNTS1 ORDER BY count DESC limit 10'

for row in cur.execute(sqlstr):
    print(str(row[0]) , row[1])
cur.close()

