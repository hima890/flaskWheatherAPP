from flask import Flask


app = Flask(__name__)
app.secret_key = 'the random string'
from watherAPP_main import routs