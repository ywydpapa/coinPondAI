from flask import Flask
import pyupbit
from comm import dbconn
import jwt
import uuid
import requests
from urllib.parse import urlencode, unquote


app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
