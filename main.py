from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hello, Google App Engine!</h1><p>Your Python app is running.</p>"

if __name__ == "__main__":
    # This is used when running locally only. 
    # When deploying to GAE, Gunicorn will serve the app.
    app.run(host="127.0.0.1", port=8080, debug=True)
