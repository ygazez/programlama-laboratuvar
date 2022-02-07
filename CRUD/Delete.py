#Delete Query

print ('Deleting user yagmur')
tsql = "DELETE FROM student WHERE name = ?"
with cursor.execute(tsql,'yagmur'):
    print ('Successfully Deleted!')
