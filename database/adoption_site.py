import os
# 没有这句的话，其他的都正常，但是在点add pup和delete pup时会报错
# 因为这两个按钮分别是add_pup和del_pup函数的链接，而这两个函数调用了forms里的两个class
from forms import AddForm, DelForm, AddOwner
from flask import Flask, render_template, url_for,redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecretkey'

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app,db)

class Puppy(db.Model):

    __tablename__ = 'puppies'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Text)
    owner = db.relationship('Owner',backref='puppy',uselist=False)

    def __init__(self,name):
        self.name = name

    def __repr__(self):
        # 如果puppies表里的owner列有数据
        if self.owner:
            return f'Puppy {self.name} has owner {self.owner.name}'
        return f'Puppy name: {self.name}'

# 要记得flask db migrate! 就是因为没有migrate和upgrade，它才会一直说找不到owners，因为我压根没把它们加入后台数据库
class Owner(db.Model):

    __tablename__ = 'owners'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Text)
    puppy_id = db.Column(db.Integer,db.ForeignKey('puppies.id'))

    def __init__(self,name,puppy_id):
        self.name = name
        self.puppy_id = puppy_id

    def __repr__(self):
        return f'Owner name: {self.name}'


####################################
#### VIEW FUNCTIONS -- HAVE FORMS ##
####################################

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/add',methods=['GET','POST'])
def add_pup():

    form = AddForm()

    if form.validate_on_submit():

        name = form.name.data

        new_pup = Puppy(name)
        db.session.add(new_pup)
        db.session.commit()

        return redirect(url_for('list_pup'))

    return render_template('add.html',form=form)


@app.route('/list')
def list_pup():
    puppies = Puppy.query.all()
    return render_template('list.html',puppies=puppies)

@app.route('/delete',methods=['GET','POST'])
def del_pup():

    form = DelForm()
    if form.validate_on_submit():
        id = form.id.data
        pup = Puppy.query.get(id)
        db.session.delete(pup)
        db.session.commit()

        return redirect(url_for('list_pup'))
    return render_template('delete.html',form=form)

@app.route('/owner',methods=['GET','POST'])
def add_owner():

    form = AddOwner()
    if form.validate_on_submit():
        puppy_id = form.puppy_id.data
        name = form.name.data
        new_owner = Owner(name,puppy_id)
        db.session.add(new_owner)
        db.session.commit()
        return redirect(url_for('list_pup'))
    return render_template('newOwner.html',form=form)

if __name__ == '__main__':
    app.run(debug=True)
