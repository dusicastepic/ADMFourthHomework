#========================== Import ==========================
from bs4 import BeautifulSoup
import requests
import re
import time
import pandas as pd
import threading

#========================== Scraping ==========================
#------- Global Variables -------
base_url = 'https://www.immobiliare.it'

list_houses_info = []
errors = []
threads_list = []
failed_urls = []

#------- Functions -------
def find_house_urls(url):
    """
    Find urls adverts looking for the tag '<a>' and the attribute 'href' 
    of the adverts inside the page
    Args:
        url (str): Web link containing the list of adverts
    Returns: 
        urls_houses_page (list): List of strings urls adverts in that page
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    urls_houses_page = []
    # Loop for every <a> tag found
    for link in soup.find_all('a'):
        data_readed = link.get('href') # Read href attribute
        # This test is to avoid problems with startswith function
        if data_readed is not None: 
            # Search only for this two url structures
            if data_readed.startswith(base_url) and re.search("/\d", data_readed):
                urls_houses_page.append(data_readed)
            #elif data_readed.startswith('/nuove_costruzioni/'):
                #urls_houses_page.append(base_url + data_readed)
    return urls_houses_page

def collect_houses_urls(n_pages=(1,10)):
    """
    Collect every advert contained in the number of pages given using 
    find_house_urls function
    Args:
        n_pages (int): Number of pages to analyze
    Returns: 
        urls_houses (list): List of strings urls adverts in all pages
    """
    urls_houses = []
    # Loop in every page to see
    for i in range(n_pages[0], n_pages[1]+1):
        analized_url = base_url + '/vendita-case/roma/?criterio=rilevanza&pag='+str(i)
        urls_houses.extend(find_house_urls(analized_url))
    print("Done: ", n_pages)
    return urls_houses

def find_information_house(url):
    """
    Find information in adverts looking for different tags:
    price, locali, superficie, bagni, piano, description
    Args:
        url (str): Web link containing the advert
    """
    # Try to read a response, if fails and response empty add url to failed_urls
    response = ""
    try:
        response = requests.get(url)
    except:
        failed_urls.append(url)
    
    # If response is correct
    if response != "":
        soup = BeautifulSoup(response.text, "lxml")
        price=locali=superficie=bagni=piano=description= ''
        house_error = []

        ## Loop for finding PRICE
        for line in soup.find_all('li'):
            data_readed = line.get('class')
            try:
                # This condition test avoid problems with startswith function
                if type(data_readed) == list and type(data_readed[0] == str):
                    # Price
                    if data_readed[0].startswith('features__price'):
                        price = line.getText('class')
            except:
                house_error.append((url, 'error in: price'))

        ## Loop for finding LOCALI, SUPERFICIE, BAGNI, PIANO
        aux = ['locali', 'superficie', 'bagni', 'piano']
        counter_span = 0
        for line in soup.find_all('ul'):
            data_readed = line.get('class')
            try:
                # This condition test avoid problems with startswith function
                if data_readed is not None:        
                    # locali, superficie, bagni
                    if 'features__list' in data_readed:
                        div_content = line.find_all('div')
                        for div in range(len(div_content)):
                            div_element = div_content[div]
                            div_element_class = div_element.get('class')
                            if div_element_class is not None:
                                if 'features__label' in div_element_class:
                                    for cat in aux:
                                        if(div_element.getText('class') == cat):
                                            if cat == 'locali':
                                                locali = line.find_all('span')[counter_span].getText('class')
                                            if cat == 'superficie':
                                                superficie = line.find_all('span')[counter_span].getText('class')
                                            if cat == 'bagni':
                                                bagni = line.find_all('span')[counter_span].getText('class')
                                            counter_span +=1
                    # piano
                    if(line.find_all('abbr')):
                        piano = line.find_all('abbr')[0].getText('class').strip()
            except:
                house_error.append((url, 'error in: locali, superficie, bagni, piano'))

        ## Loop for finding DESCRIPTION
        for line in soup.find_all('div'):
            data_readed = line.get('id')
            try:
                # This condition test avoid problems with startswith function
                if type(data_readed) == str:
                    if data_readed.startswith('description'):
                        description_title = line.find_all('div')[0].getText('div')
                        description_text = line.find_all('div')[1].find('div').getText('div')
                        description = description_title + description_text
            except:
                house_error.append((url, 'error in: description'))

        list_houses_info.append([price, locali, superficie, bagni, piano, description])
        errors.append(house_error)

def collect_information_houses(urls_houses):
    """
    Collects information for every house in the list of the given urls using 
    find_information_house function and Threading
    Args:
        urls_houses (list): List of urls of houses to analyze
    Returns: 
        list_houses_info (list): list of list of houses info
        errors (list): list of scraping errors containing url and field
        threads_list (list): status list of threads
        failed_urls (list): list of failed urls
    """
    for url_house in urls_houses:
        t = threading.Thread(name=url_house, target=find_information_house, args=(url_house,))
        threads_list.append(t)
        t.start()
        
    return list_houses_info, errors, threads_list, failed_urls