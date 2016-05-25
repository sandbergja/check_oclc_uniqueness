import csv, sys
import urllib.request as ur
from xml.etree import ElementTree as ET

wskey = 'YOUR WORLDCAT SEARCH API KEY'
threshold = 3 # Number of total holdings in Worldcat to consider this resource "unique"
zipcode = '97321'
oclc_number_header = 'oclc'

if len(sys.argv) > 1:
   file_name = sys.argv[1]
else:
   file_name = 'report.csv'
   
export_file_name = 'unique.csv'

with open(file_name) as csvfile:
   with open(export_file_name, 'wt') as export_file:
      reader = csv.DictReader(csvfile)
      csv_writer = csv.writer(export_file, delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)
      for row in reader:
         if ' ' not in row[oclc_number_header].strip():
            print(row[oclc_number_header].strip())
            i = 0
            request_url = 'http://www.worldcat.org/webservices/catalog/content/libraries/' + row[oclc_number_header].strip() + '?location=' + zipcode + '&wskey=' + wskey
            print(request_url)
            root = ET.fromstring(ur.urlopen(request_url).read())
            holdings = root.findall('holding')
            for holding in holdings:
               i += 1
            if i < threshold:
              csv_writer.writerow([row[oclc_number_header], row['call_number'], row['title']])  
