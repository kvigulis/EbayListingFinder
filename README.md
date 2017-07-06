# EbayListingFinder
Used to make customized automatic search for very specific eBay listings.

Saves the found listing in a mySQL database called "eBayLinks"

Setup:

sudo pip install MySQL-python<br>
sudo pip install selenium<br>

Download and add 'chromedriver' to the path you want. Edit line 4 in findEBayData.py to designate the correct path to 'chromedriver'.<br>
```
first_window = webdriver.Chrome("/home/carl/chromedriver")
```
Set up a XAMPP mySQL server and a webpage to display the databese contents.

For simple demo:

Copy eBayLinks folder with *.php *. files
