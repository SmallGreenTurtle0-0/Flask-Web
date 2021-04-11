from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = '4c68d00afb8323e8da579a8d'
from Web import routes