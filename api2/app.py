from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/get/legend', methods=['GET'])
def get_title():
    weapon = requests.get('http://localhost:5000/get/weapon')
    weapon_text = weapon.text
    if weapon_text == 'Claymore':
        legend = 'The unbroken'
    elif weapon_text == 'Fists':
        legend =  'The unfortunate'
    elif weapon_text == 'Spear':
        legend = 'The tribesman'
    elif weapon_text == 'Battle axe':
        legend = 'The Barbarian'
    else:
        legend = 'The Ranger'
    return render_template('home.html', title='Weapon Legend', weapon=weapon_text, legend=legend)

if __name__ == '__main__':
    app.run(port=5001, debug=True, host='0.0.0.0')