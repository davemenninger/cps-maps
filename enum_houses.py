#!/usr/bin/python

import os
import sqlite3

conn = sqlite3.connect('schools.db')

conn.execute('DROP TABLE IF EXISTS houses;')
conn.execute('''CREATE TABLE houses 
	(id INTEGER PRIMARY KEY, house_number NUMERIC, dir TEXT, street_name TEXT, zipcode TEXT, elementary TEXT, middle TEXT);''')

cursor = conn.execute('''SELECT range, dir, street_name, zipcode, elementary, middle, side FROM scrapes''')

for row in cursor:
	address_range = row[0]
	direction = row[1]
	street_name = row[2]
	zipcode = row[3]
	elementary = row[4]
	middle = row[5]
	side = row[6]

	range_begin,range_end = address_range.split("-",2)

	hn = int(range_begin)

	if side == "Odd":
		while hn <= int(range_end):
			print " ".join( (str(hn) , direction , street_name , zipcode ) )
			# Insert a row of data
			conn.execute("INSERT INTO houses VALUES ( NULL, \'" + str(hn) +  "\' , \'"  + direction +  "\' , \'"  + street_name +  "\' , \'"  + zipcode +  "\' , \'"  + elementary +  "\' , \'"  + middle + "\') ")
			hn += 2
	elif side == "Even":
		while hn <= int(range_end):
			print " ".join( (str(hn) , direction , street_name , zipcode ) )
			# Insert a row of data
			conn.execute("INSERT INTO houses VALUES ( NULL, \'" + str(hn) +  "\' , \'"  + direction +  "\' , \'"  + street_name +  "\' , \'"  + zipcode +  "\' , \'"  + elementary +  "\' , \'"  + middle + "\') ")
			hn += 2
	else:
		while hn <= int(range_end):
			print " ".join( (str(hn) , direction , street_name , zipcode ) )
			# Insert a row of data
			conn.execute("INSERT INTO houses VALUES ( NULL, \'" + str(hn) +  "\' , \'"  + direction +  "\' , \'"  + street_name +  "\' , \'"  + zipcode +  "\' , \'"  + elementary +  "\' , \'"  + middle + "\') ")
			hn += 1

conn.commit()

conn.close()