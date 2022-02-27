# This script will pull list of street suffix from USPS to create a list to 
# better parse housing/street data
import requests
from bs4 import BeautifulSoup as bs

header = {'User-Agent': 'Mozilla/5.0'}
response = requests.get('https://pe.usps.com/text/pub28/28apc_002.htm', headers=
    header)
soup = bs(response.text, 'lxml')
# navigate to table
capsule = soup.find('table', {'id':'ep533076'} )
capsule = capsule.find_all('tr')
street_suffix = []
# Step over table header and iterate through
for i in capsule[1:]:
    # add to list, splitting residual column formatting
    street_suffix += i.text.split(' ')
# remove duplicates & empty strings
street_suffix = list(dict.fromkeys(street_suffix))
street_suffix.remove('')

print(street_suffix)