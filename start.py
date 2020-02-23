from flask import Flask, render_template
from flask import jsonify
from MongoDB import connection
from TwitterAPI import twitterAPI

app=Flask(__name__)
movie="Sapiens"
@app.route('/')
def index():
   return render_template('index.html')

@app.route('/signup',methods=['GET'])
def signup():
   return render_template('signup.html')

@app.route('/bookDetails')
def bookDetails(movie):
   details=connection.search(movie)
   tweets=twitterAPI.get_tweets(movie)
   return render_template('bookDetails.html',book_details=details,tweets=tweets)

if __name__ == '__main__':
   app.run(debug = True,port=3400)