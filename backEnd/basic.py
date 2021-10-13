# 最好还是不要用jupyter来做这个，不知怎么搞的偶尔会无法使用jupyter
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello World!</h1>"

@app.route('/information')
def info():
    return "<h1>Hello Again!</h1>"

# 一个要点：flask似乎必须用双引号
@app.route('/puppy/<name>')
def other_page(name):
    return '<h1>User: {}</h1>'.format(name[100])

if __name__ == '__main__':
    # 开启debug后，就能详细看到出错的问题，在那个页面输入debug pin（在cmd可以看到）
    # 还可以直接在页面里debug
    # 但是网页面向用户后，就要把debug关掉，否则别人都能看到那个debug页面
    app.run(debug=True)
