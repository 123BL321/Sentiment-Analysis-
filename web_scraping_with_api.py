from pygooglenews import GoogleNews
from bs4 import BeautifulSoup
import requests

def organize_information(search, location):
    gn = GoogleNews(lang = 'en', country = location)
    search = gn.search(search)
    document = open("data.csv", "a")
    document.write("title, day, time, link \n")
    for item in search['entries']:
        #print(item)
        title = item.title
        title = title.replace(",", "")
        time = item.published
        link = item.link
        #description = get_description(link)
        #print(description)
        document.write("{}, {}, {} \n".format(title, time, link))

    document.close()

search = input("What would you like to search? ")
location = input("What country is this search in the context of? ")
search_dictionairies = organize_information(search, location)

 

