from flask import Flask, render_template, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
#RPi.GPIO cannot be installed on windows so i am using test data file to test pulling data from other files. Will need to be put back to TimingGates to work.
import TestData as TimingGates

app = Flask(__name__)

@app.route('/',methods=["GET","POST"])
def p():
    driver = request.form.get('textbox')
    j = len(TimingGates.t) -1
    if(driver == ""):
        driver="None"
    return render_template('HTML.html', time=TimingGates.t[j], times=TimingGates.t, driver=driver)

if __name__ == '__main__':
    app.run(debug=True)