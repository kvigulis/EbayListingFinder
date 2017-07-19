import MySQLdb

mySQLcursor = 0 # Global variables
mySQLconn = 0

def mySQLserverLogin():
    global mySQLcursor
    global mySQLconn
    #, passwd="giancoli"
    mySQLconn = MySQLdb.connect("localhost", user="root", passwd="", unix_socket="/opt/lampp/var/mysql/mysql.sock")
    mySQLcursor = mySQLconn.cursor()

def mySQL_createDatabase():
    mySQLcursor.execute("CREATE DATABASE eBayLinks")
    mySQLcursor.execute("USE eBayLinks")
    mySQLcursor.execute("CREATE TABLE laserLinks (time int(13), itemNr varchar(20), timeLeft varchar(20),"
              " price float(10), title varchar(125), URL varchar(300), imageURL varchar(300))")
    mySQLcursor.execute("CREATE TABLE Z97Links (time int(13), itemNr varchar(20), timeLeft varchar(20),"
                        " price float(10), title varchar(125), URL varchar(250), imageURL varchar(250))")
    mySQLcursor.execute("CREATE TABLE OscilloscopeLinks (time int(13), itemNr varchar(20), timeLeft varchar(20),"
                        " price float(10), title varchar(125), URL varchar(250), imageURL varchar(250))")
    mySQLcursor.execute("CREATE TABLE GPULinks (time int(13), itemNr varchar(20), timeLeft varchar(20),"
                        " price float(10), title varchar(125), URL varchar(250), imageURL varchar(250))")

def mySQL_databaseReset():
    mySQLcursor.execute("DROP DATABASE eBayLinks")
    mySQL_createDatabase()

def mySQL_useDatabese():
    mySQLcursor.execute("SHOW DATABASES LIKE 'eBayLinks'")
    if mySQLcursor.rowcount == 1:
        mySQLcursor.execute("USE eBayLinks")
    else:
        mySQL_createDatabase()