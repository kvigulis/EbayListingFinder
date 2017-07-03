import searchSetups # author: Karlis Vigulis
import findEBayData
import mySQLdb_keeper


mySQLdb_keeper.mySQLserverLogin()
#mySQLdb_keeper.mySQL_createDatabase() # Used the first time to create DB and Tables on a mySQL server.
mySQLdb_keeper.mySQL_databaseReset() # Drops any existing (populated) tables and creates them (empty) again.

# Main program:

printResultsWhileRun = True
totalMatchesFound = 0

laserUrl = "http://www.ebay.co.uk/sch/Business-Office-Industrial/" \
               "12576/i.html?_from=R40&_nkw=Laser&rt=nc&LH_ItemCondition=2500%7C3000%7C7000%7C10"
minLaserPower = 130  # Watts
maxLaserPrice = 2000  # Pounds

search1 = searchSetups.LaserSearch(minLaserPower, maxLaserPrice)
findEBayData.mainSearchMethod(search1, laserUrl, 0, printResultsWhileRun)








