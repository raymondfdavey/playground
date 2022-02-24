# https: // www.imdb.com/search/title /?groups = top_1000 & ref_ = adv_prv
import requests
from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np


headers = {"Accept-Language": "en-US, en;q=0.5"}
url = "https://www.imdb.com/search/title/?groups=top_1000&ref_=adv_prv"

results = requests.get(url, headers=headers)
soup = BeautifulSoup(results.text, "html.parser")

# initialize empty lists where you'll store your data
titles = []
years = []
time = []
imdb_ratings = []
metascores = []
votes = []
us_gross = []

# to find the right div obviously look but also within the dev tools inspect bit you can go ctrl+F and then type the class you think it is and see what it returns - i.e. you can rule out that it's not present elsewhere

movie_div = soup.find_all('div', class_='lister-item mode-advanced')


for movie in movie_div:

    name = movie.h3.a.text
    titles.append(name)

    year = movie.h3.find('span', class_='lister-item-year').text
    years.append(year)

    runtime = movie.p.find('span', class_='runtime').text if movie.p.find(
        'span', class_='runtime') else '-'
    time.append(runtime)

    rating = movie.find('strong').text
    imdb_ratings.append(float(rating))

    m_score = movie.find('span', class_='metascore').text if movie.find(
        'span', class_='metascore') else '-'
    metascores.append(m_score)

    nv = movie.find_all('span', attrs={'name': 'nv'})

    vote = nv[0].text
    votes.append(vote)

    grosses = nv[1].text if len(nv) > 1 else '-'
    us_gross.append(grosses)


movies = pd.DataFrame({
    'movie': titles,
    'year': years,
    'timeMin': time,
    'imdb': imdb_ratings,
    'metascore': metascores,
    'votes': votes,
    'us_grossMillions': us_gross,
})

# grabbing out the numbers from brackets
movies['year'] = movies['year'].str.extract('(\d+)').astype(int)
movies['timeMin'] = movies['timeMin'].str.extract('(\d+)').astype(int)

# changing to an integer
movies['metascore'] = movies['metascore'].astype(int)

# removing commas
movies['votes'] = movies['votes'].str.replace(',', '').astype(int)

# strip $ from left and M from right. lambda x just means anonymous function to be performed on each of the items in the list
movies['us_grossMillions'] = movies['us_grossMillions'].map(
    lambda x: x.lstrip('$').rstrip('M'))

# od.to_numeric changes the column to a float but can deal with the "-" entries by allowing the error parameter which here changes the dashes to NaN

movies['us_grossMillions'] = pd.to_numeric(
    movies['us_grossMillions'], errors='coerce')


print(movies)
print(movies.dtypes)
movies.to_csv('movies.csv')
