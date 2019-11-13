import pypyodbc


SQLserver = "AMIGOS-PK\SQLEXPRESS"
DBname = "roman"

connection = pypyodbc.connect('Driver={SQL Server};'
                              'Server='+SQLserver+';'
                              'Database='+DBname+';')

cursor = connection.cursor()

select = '''SELECT * FROM Table_1'''
cursor.execute(select)
data = cursor.fetchall()
connection.close()
connection = pypyodbc.connect('Driver={SQL Server};'
                              'Server='+SQLserver+';'
                              'Database='+DBname+';')
cursor = connection.cursor()
cursor.execute(select)
data_one = cursor.fetchone()
connection.close()
print(data_one, end='\n\n')
for d in data:
    print(d)