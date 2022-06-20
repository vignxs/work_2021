from fastapi import FastAPI
import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd="Vignesh26@", database = "company" )

my_cursor = mydb.cursor()
my_cursor.execute('select * from employee')
db = my_cursor.fetchall()

app = FastAPI()

@app.route("/")
def home_page():
    return render_template('index.html')

@app.get("/names")
def names():
    my_cursor.execute('select first_name from employee')
    name = my_cursor.fetchall()
    return name
