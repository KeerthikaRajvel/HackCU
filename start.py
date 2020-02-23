from flask import Flask, render_template
from flask import jsonify
from MongoDB import connection
app=Flask(__name__)


@app.route('/bookDetails')
def bookDetails():
   details=connection.search("Sapiens")
   return render_template('bookDetails.html',book_details=details)

if __name__ == '__main__':
   app.run(debug = True,port=3400)