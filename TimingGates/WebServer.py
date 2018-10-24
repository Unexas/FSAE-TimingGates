from flask import Flask, render_template
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField

yo = [
    {
        'time':'1:10.05',
        'person' : 'Eddie'
    },
    {
        'time':'1:25.21',
        'person' : 'Branson'
    }
]
time = '1:23.05'
app = Flask(__name__)

@app.route('/times')
def index():
    return render_template('HTML.html', times=yo)

@app.route('/',)
def p():
    return render_template('Name.html', time=time)

if __name__ == '__main__':
    app.run(debug=True)