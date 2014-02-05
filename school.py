#!/usr/bin/python

import urllib
import urllib2
from bs4 import BeautifulSoup

url = "http://slg.cps-k12.org/slg/school-lookup.asp"
#url = "http://slg.cps-k12.org/slg/school-lookup-nextyear.asp"

values = {
	'CurrentStep':'ShowSchools',
	'txtHouseNumber':'6631',
	'txtStreetName':'Iris Ave'
}

data = urllib.urlencode(values)
req = urllib2.Request(url, data)
response = urllib2.urlopen(req)
the_page = response.read()

soup = BeautifulSoup(the_page)

table = soup.find("table", {"border":"1"})

rows = table.findAll('tr')
for tr in rows:
  cols = tr.findAll('td')
  for td in cols:
      text = td.get_text()
      print text+"|",
  print

