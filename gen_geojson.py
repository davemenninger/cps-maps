#!/usr/bin/python

import sqlite3
import json
import hashlib

conn = sqlite3.connect('schools.db')

cursor = conn.execute('''SELECT houses.elementary, geocodes.lat, geocodes.lon 
	FROM houses, geocodes 
	WHERE houses.id = geocodes.house_id 
	ORDER BY RANDOM() 
	LIMIT 2000 ''')

geojson_string = ' { "type": "FeatureCollection", '
geojson_string += ' "features" : [ '

features = []

for row in cursor:
	elementary = row[0]
	lat = row[1]
	lon = row[2]

	marker_color = hashlib.md5(elementary.encode()).hexdigest()[:6].upper()
	
	feature_string =  ' { '
	feature_string += ' "type" : "Feature" , '
	feature_string += ' "properties" : { "elementary" : "'+elementary+'", "marker-color" : "#' + marker_color + '", "marker-size" : "small", "marker-symbol" : "school" }, '
	feature_string += ' "geometry" : { "type" : "Point" , "coordinates" : [ ' + str(lon) + ' , ' + str(lat) + ' ] } '
	feature_string += ' } '

	features.append(feature_string)

geojson_string += ",".join( features )
geojson_string += ' ] ' #end of features list
geojson_string += ' } ' #end of json

print geojson_string

conn.commit()
conn.close()