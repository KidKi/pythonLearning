import xlrd,sqlite3

data = xlrd.open_workbook("dummy_data.xlsx")
table = data.sheets()[0]
nrows = table.nrows
conn = sqlite3.connect('test.db')
cursor = conn.cursor()
# cursor.execute('drop table score')
cursor.execute('select * from sqlite_master where type=? and name=?',('table','score'))
#print(cursor.rowcount)
if cursor.rowcount==-1:
	cursor.execute('create table score(id integer primary key autoincrement,name varchar(20),score int)')
for i in range(nrows):
	if i==0:
		continue

	cursor.execute('insert into score(name,score) values (?,?)',(table.cell_value(i,0),table.cell_value(i,1)))
cursor.execute('select * from score')
print(cursor.fetchall())
cursor.close()
conn.commit()
conn.close()
	#print(table.cell_value(i,0),end=" ")
	#print(table.cell_value(i,1))
