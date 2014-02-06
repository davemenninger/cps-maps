cps-maps
========

various mapping hacks of cincinnati public school data

# Scripts

Provided is a collection of scripts that scrape data from the CPS website.  The included .sh script illustrates the order in which they'd be used to create an example geojson file.

Basically it goes like this:

1. scrape address ranges from html
2. enumerate all house numbers in those ranges ( possibly crazy )
3. geocode a random selection of these house addresses
4. generate a geojson file from the data

# Requirements

sqlite3, BeautifulSoup, geopy

# TODO

* scrape these pages: 
    * http://www.cps-k12.org/schools-print/school-list/elementary
    * http://www.cps-k12.org/schools-print/school-list/secondary
* turn the school.py script into a chrome extension?
