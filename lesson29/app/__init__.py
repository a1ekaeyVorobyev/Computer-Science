from flask import Flask

app = Flask(__name__, '/static')
app.config['SECRET_KEY'] = "asdfbjkasdfjklasdkfhjasdfhjkl"

from app import routes
