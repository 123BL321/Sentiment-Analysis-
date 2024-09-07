from pygooglenews import GoogleNews
from bs4 import BeautifulSoup
import requests



"""""
def get_titles(search):
    search = gn.search(search)

    #organizes by entries where titles and more can be extracted 
    for item in search['entries']:
        print(item.title)
        titles
    return 
"""""

#def get_description(link):
    # import the required libraries
    #base_URL = 'https://www.gamespot.com'
 
# get the news category
#category_URL = f'{base_URL}/news'
 
#response = requests.get(category_URL)
 
#data_links  = []
 
#if response.status_code == 200:
 
    # parse HTML content with BeautifulSoup
    #soup = BeautifulSoup(response.content, 'html.parser')
    #print(soup)
 
#else:
    #print(f'An error has occurred with status {response.status_code}')



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

 

