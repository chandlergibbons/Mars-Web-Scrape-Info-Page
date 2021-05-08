# web-scraping-challenge

![](Mars-Perseverance-Landing.gif)

In this project I built a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page. The following outlines what I did. 

Step 1 - Scraping

Technolgies: Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter

NASA Mars News

First I scraped the NASA Mars News Site and collected the latest News Title and Paragraph Text. I then Assigned the text to variables to be referenced later.


JPL Mars Space Images - Featured Image


Next I Visited the url for JPL Featured Space Image. I then used splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable.


Mars Facts


The next items I grabed were on the Mars Facts webpage. I used Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc. I then used Pandas to convert the data to a HTML table string.



