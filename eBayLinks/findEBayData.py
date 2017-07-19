from selenium import webdriver
from pyvirtualdisplay import Display
import re
import time

def loadEBayResults(printWhileRunning, url):

    # display = Display(visible=0, size=(1024, 768))
    # display.start()
    first_window = webdriver.Chrome("/home/carl/chromedriver")  # Search result window (main)

    # loads a webpage from an url and returns two WebElement lists to iterate through: one with titles and other with prices
    first_window.get(url)
    html_source = first_window.page_source
    html_results = html_source.split('ListViewInner')[1].split('Pagination')[0]
    html_items = html_results.split('listingid="')[1:]

    itemIDs = []
    timeLeft = []
    titles = []
    pricesAsFloat = []
    URLs = []
    imageURLs = []

    for x in range(len(html_items)):

        itemIDs.append(html_items[x].split('"')[0])

        if 'timeleft' in html_items[x]:
            timeLeft.append(html_items[x].split('timems="')[1].split('"')[0])
        else:
            timeLeft.append("Not an auction")

        titles.append(html_items[x].split('title="Click this link to access ')[1].split('">')[0])

        # Price formating is more complex because of the separator ticks and pound sign.
        priceVeryDirty = html_items[x].split('lvprice prc">')[1].split('class="bold">')[1].split('</span>')[0]
        priceDirty = priceVeryDirty.replace("\t", "").replace("\n", "")
        non_decimal = re.compile(r'[^\d.]+')
        price = float(non_decimal.sub('', str(priceDirty.encode("utf-8").rsplit(' ', 1)[0])))
        pricesAsFloat.append(price)

        URLs.append(html_items[x].split('a href="')[1].split('"')[0])

        imageURL = None
        while imageURL is None:
            try:
                # Will try till the image is loaded to get the URL
                print("Image URL:", imageURL)
                print("HTML item: ", html_items[x])
                imageURL = html_items[x].split('<img src="')[1].split('"')[0]
            except:
                try:
                    imageURL = html_items[x].split(' src="')[1].split('"')[0]
                except:
                    pass
                pass
                time.sleep(0.1)

        imageURLs.append(imageURL)

        if printWhileRunning:
            print('\n=========================\n=========================\n')
            print('listingID:')
            print(itemIDs[x])
            print(timeLeft[x])
            print(titles[x])
            print(pricesAsFloat[x])
            print(URLs[x])
            print(imageURLs[x])

    if '"Next page of results"' in html_source:
        nextPageUrl = (html_source.split('"Next page of results"')[1]
                .split('href="')[1]
                .split('">')[0]
                .replace("&lt;", "<")
                .replace("&gt;", ">")
                .replace("&amp;", "&"))
    else:
        nextPageUrl = "NoNextPage!"

    first_window.close()
    # display.stop()

    return itemIDs, timeLeft, titles, pricesAsFloat, URLs, imageURLs, nextPageUrl

def mainSearchMethod(searchType, url, printWhileRunning = False):
    # Main method that contains everything needed

    totalMatchesFound = 0
    pageNumber = 1
    nextPageUrl = url

    while nextPageUrl.find("http://") != -1 or nextPageUrl.find(
            "https://") != -1:  # Check if there is a 'https://' in the 'href' behind the 'next page arrow'
        print("\n" + "Next Page URL: " + nextPageUrl)
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

        print("\n\n" + "Page Number: " + str(pageNumber))
        print("\n" + "Matches Found: " + str(totalMatchesFound))
        print("\n" + "Matching Links:")
        for link in matchingLinks:
            print(link)
        print('\n========================================\n========================================\n')
        pageNumber += 1

    return matchingLinks










