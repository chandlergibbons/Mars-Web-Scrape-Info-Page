  # import necessary libraries
from flask import Flask, render_template, redirect
from scrape_mars import scrape
from flask_pymongo import PyMongo
# create instance of Flask app
app = Flask(__name__)

mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_page_content")

@app.route("/")
def home():

    # Find one record of data from the mongo database
    mars_page_data = mongo.db.collection.find_one()

    # Return template and data
    return render_template("index.html", scraped=mars_page_data)




@app.route("/scrape")
def pull_content():
    mars_content = scrape()
    mongo.db.collection.update({},  mars_content, upsert=True)

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)