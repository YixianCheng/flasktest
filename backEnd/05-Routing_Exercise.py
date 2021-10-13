# Set up your imports here!
# import ...
from flask import Flask

app = Flask(__name__)

@app.route('/') # Fill this in!
def index():
    # Welcome Page
    # Create a generic welcome page.
    return "<h1>Welcome!</h1>"

@app.route('/puppylatin/<name>') # Fill this in!
def puppylatin(name):
    # This function will take in the name passed
    # and then use "puppy-latin" to convert it!

    # HINT: Use indexing and concatenation of strings
    # For Example: "hello"+" world" --> "hello world"
    if name[-1].lower() == 'y':
        return f"<h1>The latin name is {name[:-1]}iful!</h1>"
    else:
        return f"<h1>The latin name is {name}y!</h1>"

if __name__ == '__main__':
    # Fill me in!
    app.run(debug=True)
