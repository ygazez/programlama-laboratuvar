import pyodbc
#connect db

server = '(LocalDB)\MSSQLLocalDB'
database = 'SampleDB'
username = ''
password = ''
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
#Insert

print ('Inserting a new row into table')
#Insert Query
tsql = "INSERT INTO student (name, location) VALUES (?,?);"
with cursor.execute(tsql,'Emre','Izmır'):
    print ('Successfully Inserted!')
