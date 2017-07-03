from selenium import webdriver
import re

first_window = webdriver.Chrome("/usr/lib/chromedriver")  # Search result window (main)
first_window.implicitly_wait(25)

def loadEBayResults(printWhileRunning, url):
    # loads a webpage from an url and returns two WebElement lists to iterate through: one with titles and other with prices
    first_window.get(url)
    resultsPanel = first_window.find_element_by_id('ListViewInner')
    resultsItems = resultsPanel.find_elements_by_class_name('sresult')
    resultsTitles = resultsPanel.find_elements_by_tag_name('h3')
    resultsPricesContainerList = resultsPanel.find_elements_by_class_name('lvprices')
    resultsImageURLs = resultsPanel.find_elements_by_class_name('lvpicinner')

    itemIDs = []
    titlesLC = []
    pricesAsFloat = []
    URLs = []
    imageURLs = []

    for i in range(len(resultsTitles)):
        currentPrice = (resultsPricesContainerList[i]
                            .find_element_by_tag_name('span')
                            .get_attribute('innerHTML')
                            .replace("\n", "")
                            .replace("\t", "")
                            .replace(" ", "")) # will take the upper price in bold
        # this will be auction price if the 'buy it now' option is available
        non_decimal = re.compile(r'[^\d.]+')
        pricesAsFloat.append(float(non_decimal.sub('', str(currentPrice.encode("utf-8")))
                                   .partition(".")[0]))
        # remove pound and comma chars to make the format as float number

        currentItemID = resultsItems[i].get_attribute('listingid')
        itemIDs.append(currentItemID)

        currentTitle = (resultsTitles[i].find_element_by_tag_name('a').get_attribute('title')[25:] + " ")
        titlesLC.append(currentTitle)  # make everything lower case so its not case sensitive

        currentUrl = resultsTitles[i].find_element_by_tag_name('a').get_attribute('href')  # finds the url of the listing's title
        URLs.append(currentUrl)

        currentImageURL = resultsImageURLs[i].find_element_by_css_selector('img').get_attribute('src')
        imageURLs.append(currentImageURL)

        if printWhileRunning:
            print("\n" + currentTitle[1:])
            print(currentItemID)
            print(currentPrice)
            print(pricesAsFloat[i])
            print(currentImageURL)

    nextPageUrl = first_window.find_element_by_id('Pagination').find_element_by_class_name('pagn-next').find_element_by_tag_name('a').get_attribute('href')

    return itemIDs, titlesLC, pricesAsFloat, URLs, imageURLs, nextPageUrl


def mainSearchMethod(searchType, url, totalMatchesFound, printWhileRunning = False):
    # Main method that contains everything needed

    nextPageUrl = url

    while nextPageUrl.find("http://") != -1 or nextPageUrl.find(
            "https://") != -1:  # Check if there is a 'https://' in the 'href' behind the 'next page arrow'

        itemIDs, titlesLC, pricesAsFloat, listingUrls, imageURLs, nextPageUrl = loadEBayResults(printWhileRunning, nextPageUrl)
        searchType.setResultsItemIDs(itemIDs)
        searchType.setTotalMatchesFound(totalMatchesFound)
        searchType.setResultsTitles(titlesLC)
        searchType.setResultsPrices(pricesAsFloat)
        searchType.setResultsURLs(listingUrls)
        searchType.setResultsImageURLs(imageURLs)
        searchType.runSearch()  # Looks for the matching items as specified by 'this' object.
        totalMatchesFound = searchType.getTotalMatchesFound()
        matchingLinks = searchType.getMatchingLaserLinks()

        print("\n\n" + "Next Page URL: " + nextPageUrl)
        print("\n" + "Matches Found: " + str(totalMatchesFound))
        print("\n" + "Matching Laser Links:")
        for link in matchingLinks:
            print(link)

    return matchingLinks










