'''
import csv
f=open('stud.csv','r')
data=csv.reader(f)
for i in data:
    print(i)
f.close()
'''

'''
import csv
with open('stud.csv','r')
    as f:
    data=csv.reader(f)
    for i in data:
        print(i)
print('data is completed')
'''

'''
import csv
with open('stud.csv','r') as f1:
    r1=csv.reader(f1)
    print('-'*80)
    for row in r1:
        print('%85' %row[0],'%85' row[1],'%85' row[2],'%85' row[3],'%85' row[4],'%85' row[5])
print("-"*60)
'''