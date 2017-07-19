from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import re

def loadEBayResults(printWhileRunning, url):

    #display = Display(visible=0, size=(1024, 768))
    #display.start()

    first_window = webdriver.Chrome("/home/carl/chromedriver")  # Search result window (main)

    # loads a webpage from an url and returns two WebElement lists to iterate through: one with titles and other with prices
    first_window.get(url)
    resultsPanel = first_window.find_element_by_id('ListViewInner')
    resultsItems = resultsPanel.find_elements_by_class_name('sresult')
    resultsTitles = resultsPanel.find_elements_by_tag_name('h3')
    resultsPricesContainerList = resultsPanel.find_elements_by_class_name('lvprices')
    resultsImageURLs = resultsPanel.find_elements_by_class_name('lvpicinner')

    itemIDs = []
    timeLeft = []
    titles = []
    pricesAsFloat = []
    URLs = []
    imageURLs = []

    for i in range(len(resultsTitles)):
        currentPrice = (resultsPricesContainerList[i]
                            .find_element_by_tag_name('span')
                            .get_attribute('innerHTML')
                            .replace("\t", "")
                            .replace("\n", ""))
                            # will take the upper price in bold
        # this will be auction price if the 'buy it now' option is available
        non_decimal = re.compile(r'[^\d.]+')
        pricesAsFloat.append(float(non_decimal.sub('', str(currentPrice.encode("utf-8").rsplit(' ', 1)[0]))))
        # remove pound and comma separator chars to make the format as float number

        currentItemID = resultsItems[i].get_attribute('listingid')
        itemIDs.append(currentItemID)

        if 'timeleft' in resultsItems[i].get_attribute('innerHTML'):
            currentTimeLeft = resultsItems[i].find_element_by_class_name('timeMs')\
                .get_attribute('timems')
            timeLeft.append(currentTimeLeft)
            print "This is an auction. Ending time: ", currentTimeLeft
        else:
            print "Not an auction"
            timeLeft.append("Not an auction")

        currentTitle = (resultsTitles[i].find_element_by_tag_name('a').get_attribute('title')[25:] + " ").encode('utf-8').decode('latin-1') # The encode & decode functions are for MySQL compatibility with some rare characters.
        titles.append(currentTitle)  # make everything lower case so its not case sensitive

        currentUrl = resultsTitles[i].find_element_by_tag_name('a').get_attribute('href')  # finds the url of the listing's title
        URLs.append(currentUrl)

        currentImageURL = resultsImageURLs[i].find_element_by_css_selector('img').get_attribute('src')
        imageURLs.append(currentImageURL)

        if printWhileRunning:
            print(currentTitle[1:])
            print(currentItemID)
            print(pricesAsFloat[i])
            print(currentImageURL + "\n")


        #nextPageUrl = url
        #TODO: remove the delay by looking into source HTML and searching 'pagination'
    try:
        nextPageUrl = first_window.find_element_by_id('Pagination').find_element_by_class_name('pagn-next').find_element_by_tag_name('a').get_attribute('href')
    except NoSuchElementException:
        nextPageUrl = "NoNextPage!"

    first_window.close()
    #display.stop()

    return itemIDs, timeLeft, titles, pricesAsFloat, URLs, imageURLs, nextPageUrl


def mainSearchMethod(searchType, url, totalMatchesFound, printWhileRunning = False):
    # Main method that contains everything needed

    nextPageUrl = url

    while nextPageUrl.find("http://") != -1 or nextPageUrl.find(
            "https://") != -1:  # Check if there is a 'https://' in the 'href' behind the 'next page arrow'

        itemIDs, timeLeft, titles, pricesAsFloat, listingUrls, imageURLs, nextPageUrl = loadEBayResults(printWhileRunning, nextPageUrl)
        searchType.setResultsItemIDs(itemIDs)
        searchType.setResultsTimeLeft(timeLeft)
        searchType.setTotalMatchesFound(totalMatchesFound)
        searchType.setResultsTitles(titles)
        searchType.setResultsPrices(pricesAsFloat)
        searchType.setResultsURLs(listingUrls)
        searchType.setResultsImageURLs(imageURLs)
        searchType.runSearch()  # Looks for the matching items as specified by 'this' object.
        totalMatchesFound = searchType.getTotalMatchesFound()
        matchingLinks = searchType.getMatchingLinks()

        print("\n\n" + "Next Page URL: " + nextPageUrl)
        print("\n" + "Matches Found: " + str(totalMatchesFound))
        print("\n" + "Matching Links:")
        for link in matchingLinks:
            print(link)

    return matchingLinks










