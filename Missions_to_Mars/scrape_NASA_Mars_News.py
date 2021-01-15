from splinter import Browser
from bs4 import BeautifulSoup


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


def scrape():
    browser = init_browser()
    listings = {}

    # Visit NASA Mars News Site
    url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    browser.visit(url)

    # Scraoe page into Soup
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    
    news_tile[""] = soup.find("a", class_="result-title").get_text()
    news_p[""] = soup.find("span", class_="result-paragraph-text").get_text()
    

    return news_title
    return news_p

