# EbayListingFinder
Used to make customized automatic search for very specific eBay listings.

Saves the found listing in a mySQL database called "eBayLinks"

Setup:<br>
sudo apt-get install libmysqlclient-dev // (if not already done)<br>
sudo pip install MySQL-python<br>
sudo pip install selenium<br>

Download and add 'chromedriver' to the path you want. Edit line 4 in findEBayData.py to designate the correct path to 'chromedriver'. <br>
```
first_window = webdriver.Chrome("/home/carl/chromedriver")
```

Also be sure to have Chrome browser installed on your server/system: https://askubuntu.com/questions/510056/how-to-install-google-chrome<br>

Set up a XAMPP mySQL server and a webpage to display the databese contents.

For a simple demo:

Copy eBayLinks folder with *.php files to path '/opt/lampp/htdocs' if you are on Linux and run the webpage by pasting http://localhost/eBayLinks/test.php in a browser. 



Appendix:

For Amazon EC2 setup: <br>
http://www.9lessons.info/2015/12/amazon-ec2-setup-with-ubuntu-and-xampp.html<br>
SFTP file transfer between the EC2 and your PC using FileZilla:<br>
http://angus.readthedocs.io/en/2014/amazon/transfer-files-between-instance.html<br>
