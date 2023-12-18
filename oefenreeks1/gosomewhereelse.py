from flask import Flask, redirect

app = Flask(__name__)

# Define a route and a function to handle requests to that route
@app.route('/')
def goSomewhereElse():
    return redirect("https://www.ap.be/", code=302)

# Run the Flask application
if __name__ == '__main__':
    app.run()