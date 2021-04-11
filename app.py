from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/checkin')
def checkin_page():
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