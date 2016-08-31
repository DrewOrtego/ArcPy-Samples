""" Creates the properties dict by scraping the online Describe Object
    documentation:
    https://pro.arcgis.com/en/pro-app/arcpy/functions/describe.htm
"""
import requests
from bs4 import BeautifulSoup as BSoup
from pprint import pprint

url = u'https://pro.arcgis.com/en/pro-app/arcpy/functions/describe.htm'
r = requests.get(url)

if r.status_code == 200:
    soup = BSoup(r.text, 'html.parser')
    xrefs = soup.find_all('a', class_='xref xref', href=True)
    header = u'https://pro.arcgis.com'
    properties = [(i.text, header + i['href']) for
                  i in xrefs if 'Properties' in i.text]
    all_attributes = dict()
    for element in properties:
        describe_property, url = element
        r = requests.get(url)
        soup = BSoup(r.text, 'html.parser')
        td_tags = soup.find_all('td')
        attributes = {t.text[:t.text.index("(Read Only)")] for
                      t in td_tags if "(Read Only)" in t.text}
        # Properties without attributes are added as an unhashable set
        # by default. This kills the parsing. Overwrite all set's to dict.
        all_attributes[describe_property] = attributes
        if all_attributes[describe_property] == set():
            all_attributes[describe_property] = dict()
else:
    print("Unable to connect to URL")
with open(os.path.join(os.getcwd(), 'default_props.py'), 'wt') as output:
    output.write(all_attributes)
print("fin.")
