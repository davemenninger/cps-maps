#!/usr/bin/python

import sqlite3
import time
from geopy import geocoders

g = geocoders.GoogleV3()

conn = sqlite3.connect('schools.db')

#conn.execute('DROP TABLE IF EXISTS geocodes;')
#conn.execute('CREATE TABLE geocodes (house_id NUMERIC, lat REAL, lon REAL);')

cursor = conn.execute('''SELECT house_number, dir, street_name, zipcode, id 
	FROM houses 
	LEFT OUTER JOIN geocodes 
	ON houses.id = geocodes.house_id 
	WHERE geocodes.house_id IS NULL 
	ORDER BY RANDOM() 
	LIMIT 100;''')

for row in cursor:
	house_number = row[0]
	direction = row[1]
	street_name = row[2]
	zipcode = row[3]
	house_id = row[4]

	address_string = " " + str(house_number) + " " + direction + " " + street_name + " " + zipcode + " "
	print "geocoding: " + address_string

 	try:
		place, (lat, lng) = g.geocode(address_string)
	except ValueError as error_message:
		print("\tError: geocode failed on input %s with message %s"%(address_string, error_message))
		continue

	print "\t%s: %.5f, %.5f" % (place, lat, lng)  

	time.sleep(1)

	conn.execute("INSERT INTO geocodes VALUES ( \'" + str(house_id) +  "\' , \'"  + str(lat) +  "\' , \'"  + str(lng) + "\') ")

	conn.commit()

conn.close()