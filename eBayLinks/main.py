import searchSetups # author: Karlis Vigulis
import findEBayData
import mySQLdb_keeper



mySQLdb_keeper.mySQLserverLogin()
#mySQLdb_keeper.mySQL_createDatabase() # Used the first time to create DB and Tables on a mySQL server.
mySQLdb_keeper.mySQL_databaseReset() # Drops any existing (populated) tables and creates them (empty) again.
mySQLdb_keeper.mySQL_useDatabese()


# Main program:

printResultsWhileRun = True
totalMatchesFound = 0

# Search setup 1:

laserUrl = "https://www.ebay.co.uk/sch/Business-Office-Industrial" \
           "/12576/i.html?_from=R40&LH_ItemCondition=2500%7C3000%7C7000%7C10&_nkw=Laser&_sop=15"
minLaserPower = 150  # Watts
maxLaserPrice = 5000.00 # Pounds
search1 = searchSetups.LaserSearch(minLaserPower, maxLaserPrice)


# Search setup 2:
AgilentOscilloscopeUrl = "https://www.ebay.co.uk/sch/Oscilloscopes-Vectorscopes/104247/i.html?_" \
                         "sop=15&_from+=R40&_udhi=200&_mPrRngCbx=1&_from=R40&_udlo=&LH_ItemCondition=4&_nkw=agilent+oscilloscope&LH_PrefLoc=2&rt=nc"
LecroyOscilloscopeUrl = "https://www.ebay.com/sch/i.html?_sop=15&_udhi=250&_mPrRngCbx=1&_from=R40&" \
                        "_sacat=0&_nkw=lecroy&_dcat=181939&rt=nc&LH_ItemCondition=7000&_trksid=p2045573.m1684"
RigolOscilloscopeUrl = "https://www.ebay.com/sch/i.html?_sop=15&_udhi=250&_mPrRngCbx=1&_from=R40&_sacat" \
                       "=0&_nkw=rigol%20oscilloscope&_dcat=104247&rt=nc&LH_ItemCondition=3000&_trksid=p2045573.m1684"
maxOscilloscopePrice = 200.00 # Pounds
search2 = searchSetups.OscilloscopeSearch(maxOscilloscopePrice)


# Search setup 3:
Z97Url = "https://www.ebay.co.uk/sch/Motherboards/1244/i.html?_from" \
       "+=R40&_mPrRngCbx=1&_udlo&_udhi=55&_sop=15&_nkw=z97&LH_PrefLoc=3&_dcat=1244&rt=nc"
maxZ97Price = 20.00 # Pounds
search3 = searchSetups.Z97Search(maxZ97Price)


# Search setup 4:
GPU1070Url = "https://www.ebay.co.uk/sch/i.html?_sop=15&_from+=R40&_udhi=300&_mPrRngCbx=1&_from" \
         "=R40&_sacat=0&_udlo&_nkw=nvidia%201070&LH_PrefLoc=3&rt=nc&_trksid=p2045573.m1684"
GPU1080Url = "https://www.ebay.co.uk/sch/i.html?_odkw=nvidia+1070&LH_PrefLoc=3&_sop=15&_from+=R40&_" \
             "udhi=300&_mPrRngCbx=1&_osacat=0&_from=R40&_trksid=p2045573.m570.l1313.TR6.TRC1.A0.H0.Xnvidia+1080.TRS0&_nkw=nvidia+1080&_sacat=0"
maxGPUPrice = 300.00 # Pounds
search4 = searchSetups.GPUSearch(maxGPUPrice)


# Run search

findEBayData.mainSearchMethod(search1, laserUrl, printResultsWhileRun)

findEBayData.mainSearchMethod(search2, AgilentOscilloscopeUrl, printResultsWhileRun)
findEBayData.mainSearchMethod(search2, LecroyOscilloscopeUrl, printResultsWhileRun)
findEBayData.mainSearchMethod(search2, RigolOscilloscopeUrl, printResultsWhileRun)

findEBayData.mainSearchMethod(search3, Z97Url, printResultsWhileRun)

findEBayData.mainSearchMethod(search4, GPU1070Url, printResultsWhileRun)
findEBayData.mainSearchMethod(search4, GPU1080Url, printResultsWhileRun)







