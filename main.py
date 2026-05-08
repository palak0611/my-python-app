from flask import Flask, render_template, request, redirect
from google.cloud import datastore

app = Flask(__name__)
datastore_client = datastore.Client()

def store_review(title, rating, comment):
    # Create a new entity for the review
    entity = datastore.Entity(key=datastore_client.key('Review'))
    entity.update({
        'title': title,
        'rating': int(rating),
        'comment': comment
    })
    datastore_client.put(entity)

def fetch_reviews():
    # Query all reviews from Datastore
    query = datastore_client.query(kind='Review')
    return list(query.fetch())

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        title = request.form['title']
        rating = request.form['rating']
        comment = request.form['comment']
        store_review(title, rating, comment)
        return redirect('/')

    reviews = fetch_reviews()
    return render_template('index.html', reviews=reviews)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
