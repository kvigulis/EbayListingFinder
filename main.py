import searchSetups # author: Karlis Vigulis
import findEBayData
import mySQLdb_keeper


mySQLdb_keeper.mySQLserverLogin()
#mySQLdb_keeper.mySQL_createDatabase() # Used the first time to create DB and Tables on a mySQL server.
mySQLdb_keeper.mySQL_databaseReset() # Drops any existing (populated) tables and creates them (empty) again.

# Main program:

printResultsWhileRun = True
totalMatchesFound = 0


# Search setup 1:
laserUrl = "http://www.ebay.co.uk/sch/Business-Office-Industrial/" \
               "12576/i.html?_from=R40&_nkw=Laser&rt=nc&LH_ItemCondition=2500%7C3000%7C7000%7C10"
minLaserPower = 150  # Watts
maxLaserPrice = 5000 # Pounds
search1 = searchSetups.LaserSearch(minLaserPower, maxLaserPrice)


# Search setup 2:
Z97Url = "https://www.ebay.co.uk/sch/Motherboards/1244/i.html?_from " \
            "=R40&_mPrRngCbx=1&_udlo=&_udhi=50&_sop=15&_nkw=z97"
maxPrice = 20 # Pounds
search2 = searchSetups.Z97Search(maxPrice)


# Run search
findEBayData.mainSearchMethod(search2, Z97Url, 0, printResultsWhileRun)






