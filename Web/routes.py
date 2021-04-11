from Web import app
from Web import forms
from Web.forms import EnterForm
from flask import render_template, url_for, redirect, request

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home_page():
    form = EnterForm()
    if request.method == 'POST':
        return redirect(url_for('checkin_page', id=form.ID))
    return render_template('home.html', form=form)

@app.route('/checkin/<string:id>')
def checkin_page(id):
    # type of id here is string
    # id to verify which (room, time, date) is this. 
    items1 = [
        {'id': 1, 'name': 'Hoang Thuy Ha', 'check': 1, 'timein': '15:30', 'image': '/static/img/test.jpg'},
        {'id': 2, 'name': 'Hoa hoa hoa', 'check': 0, 'timein': '16:30', 'image': '/static/img/test.jpg'},
        {'id': 3, 'name': 'agu gu', 'check': 1, 'timein': '17:30', 'image': '/static/img/test.jpg'},
    ]
    items2 = [
        {'id': 1, 'timein': '15:30', 'image': '/static/img/test.jpg'},
        {'id': 2, 'timein': '16:30', 'image': '/static/img/test.jpg'},
        {'id': 3, 'timein': '17:30', 'image': '/static/img/test.jpg'},
    ]
    return render_template('checkin.html', items1=items1, items2=items2)

@app.route('/personalImage/<path:img>')
def personalImage_page(img):
    return render_template('personalImage.html', image=img)