import sqlite3 as sq
conn=sq.connect('fenil.db')
print('connect')
n=int(input('enter how many records want to enter'))
i=1
while(i<=n):
    a=int(input('enter eid:-'))
    b=input('enter employee name:')
    c=int(input('salary:'))
    e=conn.execute(f"insert into emp values {a,b,c}")
    i=i+1;
conn.commit()
d=conn.execute("select * from emp")
for i in d:
    print(i)