from splinter import Browser
from bs4 import BeautifulSoup
import time


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


def scrape():
    # {} means creating a dictionary
    browser = init_browser()
    news={} # {'key': 'value', 'key2': 'value'}; news_title'[key'] return 'value'
    # news_p={}

    # Visit NASA Mars News Site
    url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    browser.visit(url)

    # Scrape page into Soup
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    # {'title': 'THIS IS THE TITLE', 'paragraph': 'THIS IS THE PARAGRAPH'}
    news_title=soup.find("li", class_="slide")#.get_text()
    print(news_title)
   # news_p=soup.find("span", class_="result-paragraph-text").get_text()
    news['title']=news_title
    # news will look like {'title': 'THIS IS THE TITLE'}
   # news["paragraph"]=news_p
    # news will look like {'title': 'THIS IS THE TITLE', 'paragraph': 'THIS IS THE PARAGRAPH'}
    
    return news
    browser=init_browser()
    
    url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    browser.visit(url)

    time.sleep(1)

    html = browser.html
    
    soup = BeautifulSoup(html, "html.parser")

    news_title= soup.find('li', class_='slide').find('div', class_='content_title').find('a').get_text()
    news_p= soup.find('li', class_='slide').find('div', class_='article_teaser_body').get_text()
    {'title': news_title, 'paragraph': news_p}
    
    featured_image_url= "https://www.jpl.nasa.gov/images/?search=&category=Mars"
    browser.visit(featured_image_url)
    
    import pandas as pd
    
    mars_facts_url = "https://space-facts.com/mars/"
    
    tables = pd.read_html(mars_facts_url)
    tables
    
    html_table = tables[0].to_html()
    html_table
    
    # USE Mongo DB to view
    # Module used to connect Python with MongoDb
    import pymongo
    # The default port used by MongoDB is 27017
    # https://docs.mongodb.com/manual/reference/default-mongodb-port/
    conn = 'mongodb://localhost:27017'
    client = pymongo.MongoClient(conn)

