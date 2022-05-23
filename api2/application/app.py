from flask import Flask, Response, request
import requests
from random import randint


app = Flask(__name__)

@app.route('/get/strength', methods=['GET'])
def post_title():
    print("hello")
    strengthNum = randint(0,10)
    strength = str(strengthNum)
    return Response(strength, mimetype = 'text/plain')

if __name__ == '__main__':
    app.run(port=5001, debug=True, host='0.0.0.0')