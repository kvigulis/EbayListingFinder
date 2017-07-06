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

    def itemFound(self, currentID, currentPriceAsFloat, currentTitle, currentUrl, currentImageURL):
        print("found")
        self.totalMatchesFound += 1
        self.matchingLaserLinks.append(currentUrl)
        mySQLdb_keeper.mySQLcursor.execute("INSERT INTO laserLinks (time, itemNr, price, title, URL, imageURL) VALUES (%s, %s, %s, %s, %s, %s)",
                  (time.time(), currentID, currentPriceAsFloat, currentTitle, currentUrl, currentImageURL, ))
        mySQLdb_keeper.mySQLconn.commit()

    def runSearch(self):
        # (This method will be designed accordingly for each 'searchType' class)
        # Must be run to append to the 'matchingLinks' list from the current page's results.


        for i in range(len(self.resultsTitles)):
            # (Titles, Prices, URLs must be lists in the same order):
            currentID = self.resultsItemIDs[i]
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
                    self.itemFound(currentID, currentPriceAsFloat, currentTitle, currentUrl, currentImageURL)

            if currentTitleLC.count(keyword6) > 0:
                if currentPriceAsFloat < self.maxLaserPrice:
                    self.itemFound(currentID, currentPriceAsFloat, currentTitle, currentUrl, currentImageURL)


class Z97Search:

    matchingZ97Links = []

    def __init__(self, maxPrice):
        # (These arguments will be different for each 'SearchType' class)

        self.maxPrice = maxPrice

    def setTotalMatchesFound(self, totalMatchesFound):
        self.totalMatchesFound = totalMatchesFound

    def setResultsItemIDs(self, resultsItemIDs): # Acquire lower case titles.
        self.resultsItemIDs = resultsItemIDs

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

    def itemFound(self, currentID, currentPriceAsFloat, currentTitle, currentUrl, currentImageURL):
        print("found")
        self.totalMatchesFound += 1
        self.matchingZ97Links.append(currentUrl)
        mySQLdb_keeper.mySQLcursor.execute("INSERT INTO Z97Links (time, itemNr, price, title, URL, imageURL) VALUES (%s, %s, %s, %s, %s, %s)",
                  (time.time(), currentID, currentPriceAsFloat, currentTitle, currentUrl, currentImageURL, ))
        mySQLdb_keeper.mySQLconn.commit()

    def runSearch(self):
        # (This method will be designed accordingly for each 'searchType' class)
        # Must be run to append to the 'matchingLinks' list from the current page's results.


        for i in range(len(self.resultsTitles)):
            # (Titles, Prices, URLs must be lists in the same order):
            currentID = self.resultsItemIDs[i]
            currentTitle = self.resultsTitles[i]
            currentTitleLC = self.resultsTitles[i].lower()
            currentPriceAsFloat = self.resultsPrices[i]
            currentUrl = self.resultsURLs[i]
            currentImageURL = self.resultsImageURLs[i]

            keyword1 = " backplate "
            keyword2 = " chip "
            keyword3 = " frame "

            if (currentTitleLC.count(keyword1) or currentTitleLC.count(keyword2) or currentTitleLC.count(keyword3)) < 1:
               if currentPriceAsFloat < self.maxPrice:
                    self.itemFound(currentID, currentPriceAsFloat, currentTitle, currentUrl, currentImageURL)

