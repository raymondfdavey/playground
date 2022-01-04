import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pandas as pd
import json

# to see about the api in the dev tools sidebar inspect the network activity then under XHR look for the /search file for the one with the keyterm request (in this case from ASDA) and then take the url and remove all of the other guff and see if it will still make a request.

urlreq = 'https://groceries.asda.com/api/items/search?keyword=yogurt'

response = urllib.request.urlopen(urlreq)
jresponse = json.load(response)

with open('asdaresp.json', 'w') as outfile:
    json.dump(jresponse, outfile, sort_keys=True, indent=4)
