import csv
from urllib.request import urlopen
import operator
import ssl
import re

def getCountryPopulationDensityMapFromCSV(file):
	f=open(file)
	map=dict()
	for row in csv.reader(f):
		if len(row)==65:
			map[row[0].lower()]=row[62]
	return map

def getCountryDeathMapFromCSV(file):
	f=open(file)
	map=dict()
	for row in csv.reader(f):
		map[row[1].lower()]=row[0]
	return map
	
densitymap=getCountryPopulationDensityMapFromCSV("density.csv")
deathmap=getCountryDeathMapFromCSV("deathctryfinal.csv")

finalmap=dict()
for key in densitymap:
	if key in deathmap:
		try:
			finalmap[key]=float(deathmap[key])/float(densitymap[key])
		except:
			pass

sorted_map = sorted(finalmap.items(), key=operator.itemgetter(1))
print(sorted_map)
