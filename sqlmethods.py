import mysql.connector
from dotenv import load_dotenv
from User import User
import os

load_dotenv()

db = mysql.connector.MySQLConnection(
    host=os.getenv("HOST"),
    user=os.getenv("USER"),
    password=os.getenv("PASSWORD"),
    database="toodoo_py"
)

def testdb():
    #testng method
        mycursor = db.cursor()
        sql = "SELECT * FROM test"
        mycursor.execute(sql)
        result = mycursor.fetchone()
        print(result)

def InsertUser(User):
    #insert users
        mycursor = db.cursor()
        sql_user_insert = """INSERT INTO users (username, password) VALUES('{}','{}')""".format(User.username,User.password)
        mycursor.execute(sql_user_insert)
        db.commit()
        print("account created!!")
        
def Inserttoodoo(item,tuple):
    #insert toodooitems
        mycursor = db.cursor()
        sql_toodoo_insert = """INSERT INTO toodoo (toodoooitem, userid) VALUES('{}',{})""".format(item,tuple[0])
        mycursor.execute(sql_toodoo_insert)
        db.commit()

def gettoodoo(tuple):
    #insert toodooitems
        mycursor = db.cursor()
        sql_toodoo_insert = "SELECT toodoooitem FROM toodoo where userid = {}".format(tuple[0])
        mycursor.execute(sql_toodoo_insert)
        result = mycursor.fetchall()
        for i in result:
            print(i[0])
        

def CheckUser(User):
    #Check for user login
    mycursor = db.cursor()
    sqlSelect= "SELECT * FROM users where username = '{}' and password = '{}'".format(User.username,User.password)
    mycursor.execute(sqlSelect)
    result = mycursor.fetchone()
    if result is None:
        return False
    else:
        return True

def GetUser(user):
    #returns the user tuple obj to be used in another method
    mycursor = db.cursor()
    sqlSelect= "SELECT * FROM users where username = '{}' and password = '{}'".format(user.username,user.password)
    mycursor.execute(sqlSelect)
    result = mycursor.fetchone()
    return result
    
account = User("fenix", "123")
result = GetUser(account)
gettoodoo(result)

        

