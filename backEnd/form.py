from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

# html里面会调用这里的函数，这里的函数反应html文件和相应网址。
@app.route('/signup_form')
def signup_form():
    return render_template('signup.html')

@app.route('/thankyou')
def thank_you():
    first = request.args.get('first')
    last = request.args.get('last')
    return render_template('thankyou.html',first=first,last=last)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')

if __name__ == '__main__':
    app.run(debug=True)

# 先通过网址进入home，home链接到signup_form，于是调用signup_form函数。这个函数返回signup页面，signup则调用了thank_you函数。
# thank_you函数能获取到signup页面收集到的信息，并且传递给thankyou页面。
# home--signup_form--signup--thank_you--thankyou
