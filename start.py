from flask import Flask, render_template, request
from flask import jsonify
from MongoDB import connection
from TwitterAPI import twitterAPI

app=Flask(__name__)
movie="Homodeous"
@app.route('/')
def index():
   return render_template('index.html')

@app.route('/signup',methods=['GET'])
def signup():
   return render_template('signup.html')

@app.route('/add_user',methods=['GET','POST'])
def add_user():
   if request.method == 'POST':
      result = request.form.to_dict()
      connection.insert_user(result)
   return render_template('index.html')

@app.route('/dashboard',methods=['GET','POST'])
def dashboard():
   if request.method == 'POST':
      result=connection.get_books()
      return render_template('dashboard.html',books=result)

@app.route('/search',methods=['GET','POST'])
def search():
   if request.method == 'POST':
      book_details=connection.search(request.form["text"])
      result=[{"_id":book_details["_id"],"image":book_details["image"]}]
      return render_template('dashboard.html',books=result)

@app.route('/bookDetails')
def bookDetails(movie):
   details=connection.search(movie)
   tweets=twitterAPI.get_tweets(movie)
   return render_template('bookDetails.html',book_details=details,tweets=tweets)

if __name__ == '__main__':
   app.run(debug = True,port=3400)