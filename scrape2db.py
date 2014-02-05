#!/usr/bin/python

import os
import urllib
import urllib2
from bs4 import BeautifulSoup
import sqlite3

conn = sqlite3.connect('schools.db')

c = conn.cursor()

c.execute('DROP TABLE IF EXISTS scrapes;')
c.execute('''CREATE TABLE scrapes
             (dir text, street_name text, side text, range text, area text, zipcode text, grades text, elementary text, middle text)''')


soup = BeautifulSoup( open("./slg-print.asp").read() )  #wget this file from the CPS website http://slg.cps-k12.org/slg/slg-print.asp

table = soup.find("table", {"border":"0"})

rows = table.findAll('tr')
for tr in rows:
  cols = tr.findAll('td')
  if  len(cols) > 1 and cols[0].get_text() != 'Dir':  #this line just skips the first row
	direction = cols[0].get_text()
  	street_name = cols[1].get_text()
  	side = cols[2].get_text()
  	address_range = cols[3].get_text()
  	area = cols[4].get_text()
  	zipcode = cols[5].get_text()
  	grades = cols[6].get_text()
  	elementary = cols[7].get_text()
  	middle = cols[8].get_text()

	c.execute("INSERT INTO scrapes VALUES (\'" + direction +  "\' , \'"  + street_name +  "\' , \'"  + side +  "\' , \'"  + address_range +  "\' , \'"  +  area +  "\' , \'"  + zipcode +  "\' , \'"  + grades +  "\' , \'"  + elementary +  "\' , \'"  + middle + "\') ")

conn.commit()

conn.close()