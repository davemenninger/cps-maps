#!/bin/bash

wget http://slg.cps-k12.org/slg/slg-print.asp

./scrape2db.py

./enum_houses.py

./geocode_houses.py

./gen_geojson.py > elementary.json

#upload to geojson.io with geojsonio-cli or geojsonio.py