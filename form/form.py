from flask import Flask, render_template, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, DateTimeField, RadioField,
                    SelectField, TextField, TextAreaField, SubmitField)

from wtforms.validators import DataRequired

app = Flask(__name__)

app.config['SECRET_KEY'] = 'mysecretkey'

# 这应该是一个用来设定表格label的地方
class InfoForm(FlaskForm):
    breed = StringField('What breed are you?', validators=[DataRequired()])
    neutered = BooleanField('Have you been neutered?')
    mood = RadioField('Please choose your mood:',
                                choices=[('mood_one','Happy'),('mood_two','Excited')])
    food_choice = SelectField(u'Pick your favorite food:',
                                choices=[('chi','Chicken'),('bf','Beef'),
                                         ('fish','Fish')])
    feedback = TextAreaField()
    submit = SubmitField('Submit')

# 有get才能获取用户输入的信息，有post才能把get到的信息输出出来
@app.route('/',methods=['GET','POST'])
def index():
    form = InfoForm()
    if form.validate_on_submit():
        # session的作用是，不同的用户发起请求时，会给他们分别形成一个session，就不会搞混
        # data指的是tuple里的第一个值，mood_one,mood_two，chi等
        session['breed'] = form.breed.data
        session['neutered'] = form.neutered.data
        session['mood'] = form.mood.data
        session['food'] = form.food_choice.data
        session['feedback'] = form.feedback.data
        # 给指定函数构造url
        # redirect的作用是导向它括号里的url，也就是url_for对thankyou函数形成的url
        # 这里如果不用url_for, 直接redirect('/thankyou')也可以，所以为什么要用它还没想清楚
        # 我猜可能是为了方便，能通过函数找到url，万一以后url改了，这里也不用动
        return redirect(url_for('thankyou'))
    return render_template('index.html',form=form)

@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')

if __name__ == '__main__':
    app.run(debug=True)
