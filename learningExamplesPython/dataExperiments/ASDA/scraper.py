from bs4 import BeautifulSoup
import urllib.request
import csv

urlpage = 'https://www.fasttrack.co.uk/league-tables/tech-track-100/league-table/'

page = urllib.request.urlopen(urlpage)

soup = BeautifulSoup(page, 'html.parser')


table = soup.find('table', attrs={'class': 'tableSorter2'})


results = table.find_all('tr')


rows = []
rows.append(['Rank', 'Company', 'Webpage', 'Description', 'Location', 'Year End',
             'Annual sales rise over 3 years', 'Latest Sales in £', 'Staff', 'Comments'])


for result in results:
    # find all columns per result
    data = result.find_all('td')
    # check that columns have data
    if len(data) == 0:
        continue
    rank = data[0].getText()
    company = data[1].getText()
    location = data[2].getText()
    yearend = data[3].getText()
    salesrise = data[4].getText()
    sales = data[5].getText()
    staff = data[6].getText()
    comments = data[7].getText()

 # extract description from the name
    companyname = data[1].find(
        'span', attrs={'class': 'company-name'}).getText()
    description = company.replace(companyname, '')
    del company
    # remove unwanted characters
    sales = sales.strip('*').strip('†').replace(',', '')
    # go to link and extract company website
    url = data[1].find('a').get('href')
    page = urllib.request.urlopen(url)
    # parse the html
    soup = BeautifulSoup(page, 'html.parser')
    # find the last result in the table and get the link
    try:
        tableRow = soup.find('table').find_all('tr')[-1]
        webpage = tableRow.find('a').get('href')
    except:
        webpage = None
    rows.append([rank, companyname, webpage, description,
                 location, yearend, salesrise, sales, staff, comments])

print(rows)

# Create csv and write rows to output file
with open('techtrack100.csv', 'w', newline='') as f_output:
    csv_output = csv.writer(f_output)
    csv_output.writerows(rows)
