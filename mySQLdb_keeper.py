import MySQLdb

mySQLcursor = 0 # Global variables
mySQLconn = 0

def mySQLserverLogin():
    global mySQLcursor
    global mySQLconn
    mySQLconn = MySQLdb.connect("127.0.0.1", "root", unix_socket="/opt/lampp/var/mysql/mysql.sock")
    mySQLcursor = mySQLconn.cursor()

def mySQL_createDatabase():
    mySQLcursor.execute("CREATE DATABASE eBayLinks")
    mySQLcursor.execute("USE eBayLinks")
    mySQLcursor.execute("CREATE TABLE laserLinks (time int(13), itemNr varchar(20),"
              " price float(10), title varchar(125), URL varchar(250), imageURL varchar(250))")
    mySQLcursor.execute("CREATE TABLE Z97Links (time int(13), itemNr varchar(20),"
                        " price float(10), title varchar(125), URL varchar(250), imageURL varchar(250))")

def mySQL_databaseReset():
    mySQLcursor.execute("DROP DATABASE eBayLinks")
    mySQL_createDatabase()