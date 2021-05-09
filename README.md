# Mars Web Scrape Info Page

![](Mars-Perseverance-Landing.gif)

In this project I built a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page. The following outlines what I did. 

Step 1 - Scraping

Technolgies: Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter

NASA Mars News: https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest

First I scraped the NASA Mars News Site and collected the latest News Title and Paragraph Text. I then Assigned the text to variables to be referenced later.


JPL Mars Space Images - Featured Image: https://www.jpl.nasa.gov/images?search=&category=Mars


Next I Visited the url for JPL Featured Space Image. I then used splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable.


Mars Facts: https://space-facts.com/mars/


The next items I grabed were on the Mars Facts webpage. I used Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc. I then used Pandas to convert the data to a HTML table string.


Mars Hemispheres: https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars ((This sign is currently down and may cause issues))


Lastly I visited the USGS Astrogeology site here to obtain high resolution images for each of Mar's hemispheres.


I used splinter to click each of the links to the hemispheres in order to find the image url to the full resolution image.


I then saved both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. I used a Python dictionary to store the data.


Then I appended the dictionary with the image url string and the hemisphere title to a list. This list contains one dictionary for each hemisphere.


Step 2 - MongoDB and Flask Application

First I utilized MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.


I then converted my Jupyter notebook into a Python script with a function called scrape that will execute all of the scraping code from above and return one Python dictionary containing all of the scraped data.


Next, I built a route called /scrape that will import the python script and called my scrape function.

I Stored the return value in Mongo as a Python dictionary.


Next I created a root route / that queries my your Mongo database and passes the mars data into an HTML template to display the data.


Lastly I custom built a template HTML file called index.html that takes the mars data dictionary and display's all of the data in the appropriate HTML elements. 

Here's what the final product looked like!

![](https://github.com/chandlergibbons/Mars-Web-Scrape-Info-Page/blob/a9ab8837cd839dab82dcb30862613ecc3ca1b91c/finished_page_images/Screen%20Shot%202021-02-27%20at%2010.34.24%20PM.png)
