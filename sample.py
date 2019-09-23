import xml.etree.ElementTree as ET
from xml.etree.ElementTree import fromstring
import csv

tree = ET.parse('sample.xml')
root = tree.getroot()

orgdict = {}
orglist = []
datlist = []

csv_columns = ['TITLE','ARTIST','COUNTRY','COMPANY','PRICE','YEAR']

count = 0
for child in root:
	orgdata = {}
	for sub in child:
		if sub.attrib.get('NAME') == 'TITLE':
			orgdata['TITLE'] = sub.text
		if sub.attrib.get('NAME') == 'ARTIST':
			orgdata['ARTIST'] = sub.text
		if sub.attrib.get('NAME') == 'COUNTRY':
			orgdata['COUNTRY'] = sub.text
		if sub.attrib.get('NAME') == 'COMPANY':
			orgdata['COMPANY'] = sub.text
		if sub.attrib.get('NAME') == 'PRICE':
			orgdata['PRICE'] = sub.text
		if sub.attrib.get('NAME') == 'YEAR':
			orgdata['YEAR'] = sub.text
		tocsv = orgdata
	orglist.append(orgdata)

df = pd.DataFrame(orglist)
df.drop_duplicates(inplace=True)
print(df)
