import mySQLdb_keeper
import time

class LaserSearch:

    matchingLaserLinks = []

    def __init__(self, minLaserPower, maxLaserPrice):
        # (These arguments will be different for each 'SearchType' class)
        self.minLaserPower = minLaserPower
        self.maxLaserPrice = maxLaserPrice

    def setTotalMatchesFound(self, totalMatchesFound):
        self.totalMatchesFound = totalMatchesFound

    def setResultsItemIDs(self, resultsItemIDs): # Acquire lower case titles.
        self.resultsItemIDs = resultsItemIDs

    def setResultsTimeLeft(self, resultsTimeLeft):
        self.resultsTimeLeft = resultsTimeLeft

    def setResultsTitles(self, resultsTitles): # Acquire lower case titles.
        self.resultsTitles = resultsTitles

    def setResultsPrices(self, resultsPrices): # Acquire prices as floats
        self.resultsPrices = resultsPrices

    def setResultsURLs(self, resultsURLs): # Acquire URLs
        self.resultsURLs = resultsURLs

    def setResultsImageURLs(self, resultsImageURLs): # Acquire URLs
        self.resultsImageURLs = resultsImageURLs

    def getTotalMatchesFound(self):
        return self.totalMatchesFound

    def getMatchingLinks(self):
        return self.matchingLaserLinks

    def itemFound(self, currentID, currentTimeLeft, currentPriceAsFloat, currentTitle, currentUrl, currentImageURL):
        print("found")
        self.totalMatchesFound += 1
        self.matchingLaserLinks.append(currentUrl)
        query = "SELECT * from laserLinks where itemNr="
        tmp_query = query+currentID
        mySQLdb_keeper.mySQLcursor.execute(tmp_query)
        if mySQLdb_keeper.mySQLcursor.rowcount == 1:
            print ("This listing already exists in the table, therefore it was deleted.")
            d_query = "DELETE FROM laserLinks where itemNr="
            tmp_d_query = d_query + currentID
            mySQLdb_keeper.mySQLcursor.execute(tmp_d_query)
        mySQLdb_keeper.mySQLcursor.execute("INSERT INTO laserLinks (time, itemNr, timeLeft, price, title, URL, imageURL) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                  (time.time(), currentID, currentTimeLeft, currentPriceAsFloat, currentTitle, currentUrl, currentImageURL))
        mySQLdb_keeper.mySQLconn.commit()

    def runSearch(self):
        # (This method will be designed accordingly for each 'searchType' class)
        # Must be run to append to the 'matchingLinks' list from the current page's results.


        for i in range(len(self.resultsTitles)):
            # (Titles, Prices, URLs must be lists in the same order):
            currentID = self.resultsItemIDs[i]
            currentTimeLeft = self.resultsTimeLeft[i]
            currentTitle = self.resultsTitles[i]
            currentTitleLC = self.resultsTitles[i].lower()
            currentPriceAsFloat = self.resultsPrices[i]
            currentUrl = self.resultsURLs[i]
            currentImageURL = self.resultsImageURLs[i]

            keyword6 = " metal cutter "

            for power in range(2000):
                keyword1 = " " + str(power + self.minLaserPower) + "w "
                keyword2 = " " + str(power + self.minLaserPower) + " w "
                keyword3 = " " + str(power + self.minLaserPower) + "kw "
                keyword4 = " " + str(power + self.minLaserPower) + " kw "
                keyword5 = " saw " # used to ignore titles with 'saw'

                if (currentTitleLC.count(keyword1) > 0 or currentTitleLC.count(keyword2) > 0 \
                        or currentTitleLC.count(keyword3) > 0 or currentTitleLC.count(keyword4) > 0) \
                    and currentPriceAsFloat < self.maxLaserPrice and currentTitleLC.count(keyword5) == 0:
                    self.itemFound(currentID, currentTimeLeft, format(currentPriceAsFloat, '.2f'), currentTitle, currentUrl, currentImageURL)
                    break
                elif currentTitleLC.count(keyword6) > 0:
                    if currentPriceAsFloat <= self.maxLaserPrice:
                        self.itemFound(currentID, currentTimeLeft, format(currentPriceAsFloat, '.2f'), currentTitle,
                                       currentUrl, currentImageURL)





class OscilloscopeSearch:

    matchingOscilloscopeLinks = []

    def __init__(self, maxPrice):
        # (These arguments will be different for each 'SearchType' class)

        self.maxPrice = maxPrice

    def setTotalMatchesFound(self, totalMatchesFound):
        self.totalMatchesFound = totalMatchesFound

    def setResultsItemIDs(self, resultsItemIDs): # Acquire lower case titles.
        self.resultsItemIDs = resultsItemIDs

    def setResultsTimeLeft(self, resultsTimeLeft):
        self.resultsTimeLeft = resultsTimeLeft

    def setResultsTitles(self, resultsTitles): # Acquire lower case titles.
        self.resultsTitles = resultsTitles

    def setResultsPrices(self, resultsPrices): # Acquire prices as floats
        self.resultsPrices = resultsPrices

    def setResultsURLs(self, resultsURLs): # Acquire URLs
        self.resultsURLs = resultsURLs

    def setResultsImageURLs(self, resultsImageURLs): # Acquire URLs
        self.resultsImageURLs = resultsImageURLs

    def getTotalMatchesFound(self):
        return self.totalMatchesFound

    def getMatchingLinks(self):
        return self.matchingOscilloscopeLinks

    def itemFound(self, currentID, currentTimeLeft, currentPriceAsFloat, currentTitle, currentUrl, currentImageURL):
        print("found")
        self.totalMatchesFound += 1
        self.matchingOscilloscopeLinks.append(currentUrl)
        query = "SELECT * from OscilloscopeLinks where itemNr="
        tmp_query = query + currentID
        mySQLdb_keeper.mySQLcursor.execute(tmp_query)
        if mySQLdb_keeper.mySQLcursor.rowcount == 1:
            print ("This listing already exists in the table, therefore it was deleted.")
            d_query = "DELETE FROM OscilloscopeLinks where itemNr="
            tmp_d_query = d_query + currentID
            mySQLdb_keeper.mySQLcursor.execute(tmp_d_query)
        mySQLdb_keeper.mySQLcursor.execute("INSERT INTO OscilloscopeLinks (time, itemNr, timeLeft, price, title, URL, imageURL) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                  (time.time(), currentID, currentTimeLeft, currentPriceAsFloat, currentTitle, currentUrl, currentImageURL))
        mySQLdb_keeper.mySQLconn.commit()

    def runSearch(self):
        # (This method will be designed accordingly for each 'searchType' class)
        # Must be run to append to the 'matchingLinks' list from the current page's results.


        for i in range(len(self.resultsTitles)):
            # (Titles, Prices, URLs must be lists in the same order):
            currentID = self.resultsItemIDs[i]
            currentTimeLeft = self.resultsTimeLeft[i]
            currentTitle = self.resultsTitles[i]
            currentTitleLC = self.resultsTitles[i].lower()
            currentPriceAsFloat = float(self.resultsPrices[i])
            currentUrl = self.resultsURLs[i]
            currentImageURL = self.resultsImageURLs[i]

            keyword1 = " 54624a "
            keyword2 = " lc534a "
            keyword3 = " 5102ca "


            if (currentTitleLC.count(keyword1) or currentTitleLC.count(keyword2)
                or currentTitleLC.count(keyword3)) > 0:
               if currentPriceAsFloat <= self.maxPrice:
                    self.itemFound(currentID, currentTimeLeft, format(currentPriceAsFloat, '.2f'), currentTitle, currentUrl, currentImageURL)


class Z97Search:

    matchingZ97Links = []

    def __init__(self, maxPrice):
        # (These arguments will be different for each 'SearchType' class)

        self.maxPrice = maxPrice

    def setTotalMatchesFound(self, totalMatchesFound):
        self.totalMatchesFound = totalMatchesFound

    def setResultsItemIDs(self, resultsItemIDs): # Acquire lower case titles.
        self.resultsItemIDs = resultsItemIDs

    def setResultsTimeLeft(self, resultsTimeLeft):
        self.resultsTimeLeft = resultsTimeLeft

    def setResultsTitles(self, resultsTitles): # Acquire lower case titles.
        self.resultsTitles = resultsTitles

    def setResultsPrices(self, resultsPrices): # Acquire prices as floats
        self.resultsPrices = resultsPrices

    def setResultsURLs(self, resultsURLs): # Acquire URLs
        self.resultsURLs = resultsURLs

    def setResultsImageURLs(self, resultsImageURLs): # Acquire URLs
        self.resultsImageURLs = resultsImageURLs

    def getTotalMatchesFound(self):
        return self.totalMatchesFound

    def getMatchingLinks(self):
        return self.matchingZ97Links

    def itemFound(self, currentID, currentTimeLeft, currentPriceAsFloat, currentTitle, currentUrl, currentImageURL):
        print("found")
        self.totalMatchesFound += 1
        self.matchingZ97Links.append(currentUrl)
        query = "SELECT * from Z97Links where itemNr="
        tmp_query = query + currentID
        mySQLdb_keeper.mySQLcursor.execute(tmp_query)
        if mySQLdb_keeper.mySQLcursor.rowcount == 1:
            print ("This listing already exists in the table, therefore it was deleted.")
            d_query = "DELETE FROM Z97Links where itemNr="
            tmp_d_query = d_query + currentID
            mySQLdb_keeper.mySQLcursor.execute(tmp_d_query)
        mySQLdb_keeper.mySQLcursor.execute("INSERT INTO Z97Links (time, itemNr, timeLeft, price, title, URL, imageURL) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                  (time.time(), currentID, currentTimeLeft, currentPriceAsFloat, currentTitle, currentUrl, currentImageURL))
        mySQLdb_keeper.mySQLconn.commit()

    def runSearch(self):
        # (This method will be designed accordingly for each 'searchType' class)
        # Must be run to append to the 'matchingLinks' list from the current page's results.


        for i in range(len(self.resultsTitles)):
            # (Titles, Prices, URLs must be lists in the same order):
            currentID = self.resultsItemIDs[i]
            currentTimeLeft = self.resultsTimeLeft[i]
            currentTitle = self.resultsTitles[i]
            currentTitleLC = self.resultsTitles[i].lower()
            currentPriceAsFloat = float(self.resultsPrices[i])
            currentUrl = self.resultsURLs[i]
            currentImageURL = self.resultsImageURLs[i]

            keyword1 = " backplate "
            keyword2 = " chip "
            keyword3 = " frame "
            keyword4 = " shield "
            keyword5 = " amplifier "
            keyword6 = " cover "
            keyword7 = " panel "

            if (currentTitleLC.count(keyword1) or currentTitleLC.count(keyword2) or currentTitleLC.count(keyword3)
                or currentTitleLC.count(keyword4) or currentTitleLC.count(keyword5)
                or currentTitleLC.count(keyword6) or currentTitleLC.count(keyword7)) < 1:
               if currentPriceAsFloat <= self.maxPrice:
                    self.itemFound(currentID, currentTimeLeft, format(currentPriceAsFloat, '.2f'), currentTitle, currentUrl, currentImageURL)


class GPUSearch:

    matchingGPULinks = []

    def __init__(self, maxPrice):
        # (These arguments will be different for each 'SearchType' class)

        self.maxPrice = maxPrice

    def setTotalMatchesFound(self, totalMatchesFound):
        self.totalMatchesFound = totalMatchesFound

    def setResultsItemIDs(self, resultsItemIDs): # Acquire lower case titles.
        self.resultsItemIDs = resultsItemIDs

    def setResultsTimeLeft(self, resultsTimeLeft):
        self.resultsTimeLeft = resultsTimeLeft

    def setResultsTitles(self, resultsTitles): # Acquire lower case titles.
        self.resultsTitles = resultsTitles

    def setResultsPrices(self, resultsPrices): # Acquire prices as floats
        self.resultsPrices = resultsPrices

    def setResultsURLs(self, resultsURLs): # Acquire URLs
        self.resultsURLs = resultsURLs

    def setResultsImageURLs(self, resultsImageURLs): # Acquire URLs
        self.resultsImageURLs = resultsImageURLs

    def getTotalMatchesFound(self):
        return self.totalMatchesFound

    def getMatchingLinks(self):
        return self.matchingGPULinks

    def itemFound(self, currentID, currentTimeLeft, currentPriceAsFloat, currentTitle, currentUrl, currentImageURL):
        print("found")
        self.totalMatchesFound += 1
        self.matchingGPULinks.append(currentUrl)
        query = "SELECT * from GPULinks where itemNr="
        tmp_query = query + currentID
        mySQLdb_keeper.mySQLcursor.execute(tmp_query)
        if mySQLdb_keeper.mySQLcursor.rowcount == 1:
            print ("This listing already exists in the table, therefore it was deleted.")
            d_query = "DELETE FROM GPULinks where itemNr="
            tmp_d_query = d_query + currentID
            mySQLdb_keeper.mySQLcursor.execute(tmp_d_query)
        mySQLdb_keeper.mySQLcursor.execute("INSERT INTO GPULinks (time, itemNr, timeLeft, price, title, URL, imageURL) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                  (time.time(), currentID, currentTimeLeft, currentPriceAsFloat, currentTitle, currentUrl, currentImageURL))
        mySQLdb_keeper.mySQLconn.commit()

    def runSearch(self):
        # (This method will be designed accordingly for each 'searchType' class)
        # Must be run to append to the 'matchingLinks' list from the current page's results.


        for i in range(len(self.resultsTitles)):
            # (Titles, Prices, URLs must be lists in the same order):
            currentID = self.resultsItemIDs[i]
            currentTimeLeft = self.resultsTimeLeft[i]
            currentTitle = self.resultsTitles[i]
            currentTitleLC = self.resultsTitles[i].lower()
            currentPriceAsFloat = float(self.resultsPrices[i])
            currentUrl = self.resultsURLs[i]
            currentImageURL = self.resultsImageURLs[i]

            # including these
            keyword1 = " 1070 "
            keyword2 = " 1080 "
            keyword3 = " 1080 Ti "

            # excluding these
            keyword4 = " para "
            keyword5 = " backplate "
            keyword6 = " backplate: "
            keyword7 = " 1gb "
            keyword8 = " 2gb "
            keyword9 = " 970 "
            keyword10 = " 1050 "
            keyword11 = " 1060 "
            keyword12 = " acrylic "
            keyword13 = " cooler only "
            keyword14 = " bridge "


            if (((currentTitleLC.count(keyword1) or currentTitleLC.count(keyword2)
                or currentTitleLC.count(keyword3)) > 0)
                and ((currentTitleLC.count(keyword4)+currentTitleLC.count(keyword5)
                + currentTitleLC.count(keyword6) + currentTitleLC.count(keyword7)
                + currentTitleLC.count(keyword8) + currentTitleLC.count(keyword9)
                + currentTitleLC.count(keyword10) + currentTitleLC.count(keyword11)
                + currentTitleLC.count(keyword12) + currentTitleLC.count(keyword13)
                + currentTitleLC.count(keyword14)) < 1)):
               if currentPriceAsFloat <= self.maxPrice:
                    self.itemFound(currentID, currentTimeLeft, format(currentPriceAsFloat, '.2f'), currentTitle, currentUrl, currentImageURL)

