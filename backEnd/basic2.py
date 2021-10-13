from flask import Flask, render_template

app = Flask(__name__)
# 注意，要用render_template的话，就要把html文件放在templates文件夹里
# templates文件夹是我自己建的
@app.route('/')
def index():
    # 这两句就按照普通def看待
    name = "Cheng"
    letters = list(name)
    mylist = [1,2,3,4,5]
    user_logged_in = True
    # 这两句就相当于给返回的数据命一个名，以便在html调用
    return render_template('basic2.html', name=name, letters=letters,mylist=mylist,user_logged_in=user_logged_in)

if __name__ == '__main__':
    app.run(debug=True)
