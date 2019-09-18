import xml.etree.ElementTree as ET
from xml.etree.ElementTree import fromstring
import csv

tree = ET.parse('sample.xml')
root = tree.getroot()

orgdict = {}
orgdata = {}
orglist = []
datlist = []

csv_columns = ['TITLE','ARTIST','COUNTRY','COMPANY','PRICE','YEAR']

count = 0
for child in root:
	for sub in child:
		if sub.attrib.get('NAME') == 'TITLE':
#			orgdata['TITLE'] = sub.attrib.get('TITLE')
			orgdata['TITLE'] = sub.text
		if sub.attrib.get('NAME') == 'ARTIST':
#			orgdata['ARTIST'] = sub.attrib.get('ARTIST')
			orgdata['ARTIST'] = sub.text
		if sub.attrib.get('NAME') == 'COUNTRY':
#			orgdata['COUNTRY'] = sub.attrib.get('COUNTRY')
			orgdata['COUNTRY'] = sub.text
		if sub.attrib.get('NAME') == 'COMPANY':
#			orgdata['COMPANY'] = sub.attrib.get('COMPANY')
			orgdata['COMPANY'] = sub.text
		if sub.attrib.get('NAME') == 'PRICE':
#			orgdata['PRICE'] = sub.attrib.get('PRICE')
			orgdata['PRICE'] = sub.text
		if sub.attrib.get('NAME') == 'YEAR':
#			orgdata['YEAR'] = sub.attrib.get('YEAR')
			orgdata['YEAR'] = sub.text
            
            sample_list = orgdata
			print(orgdata)
			tocsv = orglist
			print(tocsv)
			k = tocsv[0].keys()
			with open('orgfile.txt','w+') as csvfile:
				dic = csv.DictWriter(csvfile,k,delimiter='|',extrasaction='ignore')
				dic.writeheader()
				dic.writerows(tocsv)
