#updating 

print ('Updating Location for yagmur')
tsql = "UPDATE student SET location = ? WHERE Name = ?"
with cursor.execute(tsql,'Antalya','yagmur'):
    print ('Successfully Updated!')
