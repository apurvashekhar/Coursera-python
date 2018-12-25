#Scraping Numbers from HTML using BeautifulSoup
#In this assignment you will write a Python program
#similar to http://www.pythonlearn.com/code/urllink2.py.
#The program will use urllib to read the HTML from the data files below,
#and parse the data, extracting numbers and compute the
#sum of the numbers in the file.
#We provide two files for this assignment.
#One is a sample file where we give you the sum for your testing and
#the other is the actual data you need to process for the assignment.
#Sample data: http://python-data.dr-chuck.net/comments_42.html (Sum=2553)
#Actual data: http://python-data.dr-chuck.net/comments_353539.html (Sum ends with 63)
#You do not need to save these files to your folder since your program
#will read the data directly from the URL. Note: Each student will have a
#distinct data url for the assignment - so only use your own data url for analysis.

import urllib.request as ur
from bs4 import *

url = input('Enter the url to scrape - ')

html = ur.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

count_of_spans = 0
total = 0

spans = soup('span')
for span in spans:
    total += int(span.contents[0])
    count_of_spans += 1

print('Count ', count_of_spans)
print('Sum ', total)
