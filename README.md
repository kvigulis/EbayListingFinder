# EbayListingFinder
Used to make customized automatic search for very specific eBay listings.

Saves the found listing in a mySQL database called "eBayLinks"

Setup:

sudo pip install MySQL-python<br>
sudo pip install selenium<br>

download and add "chromedriver" to the correct path.

line 4 in findEBayData.py<br>
```
first_window = webdriver.Chrome("/home/karlis/chromedriver")
```
