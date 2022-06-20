


# import mysql.connector
#import yaml
#import pandas
#from dbConnect import DBConnect

# with open('config.yaml') as file:
#     schema = "DBPASS"
#     DBConfig = yaml.safe_load(file)
#     var = DBConfig[schema]
#     print(var)
#     host, user, passwd = var.values()
#     conn_string = f"host={host} user={user} password={passwd}"

# mydb = mysql.connector.connect(conn_string)

# my_cursor = mydb.cursor()
# my_cursor.execute('select first_name from employee')

# for i in my_cursor:
#     print(i)
import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", passwd="Vignesh26@", database = "company" )

my_cursor = mydb.cursor()
my_cursor.execute('select * from employee')
db = my_cursor.fetchall()
print(db)