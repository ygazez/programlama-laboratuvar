#Select Query
print ('Reading data from table')
tsql = "SELECT id,name, location FROM student;"
with cursor.execute(tsql):
    row = cursor.fetchone()
    while row:
        print (str(row[0]) + " " + str(row[1])+ " " + str(row[2]))
        row = cursor.fetchone()
        
cnxn.close() # closing       
        
