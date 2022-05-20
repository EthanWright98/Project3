from flask import Flask, Response
from random import randint

app = Flask(__name__)

@app.route('/get/weapon', methods =['GET'])
def get_weapon():
    weapons = ['Claymore', 'Fists', 'Spear', 'Battle axe', 'Bow']
    return Response(weapons[randint(0,4)], mimetype='text/plain')

if __name__ == '__main__':
    app.run(port=5000, debug=True, host='0.0.0.0')