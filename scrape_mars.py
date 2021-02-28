def scrape ():
    from bs4 import BeautifulSoup as bs
    import pandas as pd
    from splinter import Browser
    from webdriver_manager.chrome import ChromeDriverManager
    import requests
    import time

    # URL of page to be scraped and way to get there
    url = 'https://mars.nasa.gov/news/'
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    browser.visit(url)  


    html = browser.html

    #pars out text needed 
    time.sleep(10)
    soup = bs(html, 'html.parser')
    
    results = soup.find('li', class_="slide")

    news_title = results.find('h3').text

    news_p = results.find('div', class_="article_teaser_body").text

    browser.quit()

    # URL of page to be scraped
    url2 = 'https://www.jpl.nasa.gov/images?search=&category=Mars'
    
    #click through
    browser = Browser('chrome', **executable_path, headless=False)
    browser.visit(url2)
    sort_by = browser.find_by_id('searchHelpers_sortBy')
    sort_by.select('latestDate')
    browser.find_by_id('filter_Mars').click()
    colresults = browser.find_by_id('SearchListingPageResults')
    latest_photo_page = colresults.find_by_tag('a').first
    latest_photo_page.click()
    links_found = browser.links.find_by_partial_href('images/jpeg')
    links_found.click()

    #pars out code for image 
    html2 = browser.html

    time.sleep(10)
    soup2 = bs(html2, 'html.parser')

    featured_image_url = soup2.find('img')['src']

    browser.quit()

    # URL of page to be scraped
    url3 = "https://space-facts.com/mars/"
    
    # scrap modify and store table with pandas
    tables = pd.read_html(url3)
    df = tables[0]
    df = df.rename(columns={0: "Description", 1: "Mars"})

    mars_table = df.to_html(index=False)

    browser.quit()

    # URL of page to be scraped
    url4 = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser = Browser('chrome', **executable_path, headless=False)
    # click through and parising 
    browser.visit(url4)
    browser.links.find_by_partial_text('Cerberus Hemisphere').click()

    html3 = browser.html

    time.sleep(10)
    soup3 = bs(html3, 'html.parser')

    Cerberus_Hemisphere = soup3.find('img', class_="wide-image")['src']

    browser.back()
    browser.links.find_by_partial_text('Schiaparelli Hemisphere').click()

    html4 = browser.html

    time.sleep(10)
    soup4 = bs(html4, 'html.parser')
    
    Schiaparelli_Hemisphere = soup4.find('img', class_="wide-image")['src']

    browser.back()
    browser.links.find_by_partial_text('Syrtis Major Hemisphere').click()

    html5 = browser.html

    time.sleep(10)
    soup5 = bs(html5, 'html.parser')

    Syrtis_Major_Hemisphere = soup5.find('img', class_="wide-image")['src']

    browser.back()
    browser.links.find_by_partial_text('Valles Marineris Hemisphere').click()

    html6 = browser.html

    time.sleep(10)
    soup6 = bs(html6, 'html.parser')

    Valles_Marineris_Hemisphere = soup6.find('img', class_="wide-image")['src']

    browser.quit()

    #python nested dict build out 

    base_hem = "https://astrogeology.usgs.gov"

    hemisphere_image_urls = [
    {"title": "Valles Marineris Hemisphere", "img_url": base_hem + Valles_Marineris_Hemisphere},
    {"title": "Cerberus Hemisphere", "img_url": base_hem + Cerberus_Hemisphere},
    {"title": "Schiaparelli Hemisphere", "img_url": base_hem + Schiaparelli_Hemisphere},
    {"title": "Syrtis Major Hemisphere", "img_url": base_hem + Syrtis_Major_Hemisphere}]


    mars_info2 = {
        'news_title': news_title,
        'news_p': news_p,
        "featured_image_url": featured_image_url,
        "mars_facts": mars_table,
        "hemisphere_image_urls": hemisphere_image_urls
    }

    return mars_info2
    


  

