from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/weapon/legend', methods = ['GET'])
def get_gladiator():
    weapon = requests.get('http://localhost:5000/get/weapon').text
    strength = requests.get('http://localhost:5001/get/strength').text
    generate = weapon + ' ' + strength
    chance = requests.post ('http://localhost:5002/post/chance', data = generate).text
    return render_template('home.html', title='Gladiator generator', weapon = weapon, strength = strength, chance = chance)

if __name__ == '__main__':
    app.run(port=5003, debug=True, host = '0.0.0.0')
    

