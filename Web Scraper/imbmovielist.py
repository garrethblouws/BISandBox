# Web scrap data for over 200 movies      date created:05/03/2020
import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup 

my_url = 'https://www.imdb.com/search/title/?release_date=2019&sort=num_votes,desc&page=1'

#open up connection, grabbing the page

uClient = uReq(my_url)

page_html = uClient.read()

#close connection
uClient.close()

#html parser
page_soup = soup(page_html, "html.parser")

#grabs items
containers = page_soup.findAll('div',class_ = 'lister-item mode-advanced')

filename = "imdbrating.csv"

f = open(filename,"w")

headers = "Movie, Year_Released, Genre, Rating, Votes \n"

f.write(headers)


for container in containers:
    #name of the movie
    name = container.h3.a.text.strip()
    
    #Year released 
    year = container.h3.find('span',class_ = 'lister-item-year text-muted unbold').text
    
    #Genre
    genre = container.p.find('span', class_ = 'genre').text.strip()

    #rating
    imdb = float(container.strong.text)

    #votes for each movie
    vote = container.find('span', attrs = {'name':'nv'})['data-value']
     
    f.write(name + "," + year + "," + genre.replace(",","|") + "," + str(imdb) + "," + str(vote) + "\n")

f.close()   
print("File loaded - Please check CSV file") 