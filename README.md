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
