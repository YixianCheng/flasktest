from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    # This home page should have the form.
    return render_template('homepage.html')


# This page will be the page after the form
@app.route('/report')
def report():
    # Check the user name for the 3 requirements.
    username = request.args.get('username')
    lower = False
    upper = False
    number = False

    number = username[-1].isdigit()
    for i in username:
        if i.islower():
            lower = True
            break
    for i in username:
        if i.isupper():
            upper = True
            break
    if number and lower and upper:
        return render_template('reportpass.html')
    else:
        return render_template('reportfail.html',number=number,upper=upper,lower=lower)
    # HINTS:
    # https://stackoverflow.com/questions/22997072/how-to-check-if-lowercase-letters-exist/22997094
    # https://stackoverflow.com/questions/26515422/how-to-check-if-last-character-is-integer-in-raw-input

    # Return the information to the report page html.

if __name__ == '__main__':
    # Fill this in!
    app.run(debug=True)
