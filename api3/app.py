from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/post/chance', methods=['POST'])
def post_chance():
    generate = request.data.decode('utf-8')
    favour= generate.split()
    if chance[0] == 'Claymore' and chance[0] == 'The unbroken':
        favour = 'Thumbs up, you survive'
    elif chance[1] == 'Fists' and chance[1] == 'The unfortunate':
        favour = 'Thumbs down, you have been defeated'
    elif chance[2] == 'Spear' and chance[2] == 'The tribesman':
        favour = 'Thumbs up, you survive'
    elif chance[3] == 'Battle axe' and chance[3] == 'The barbarian':
        favour = 'Thumbs up, you survive'
    elif chance[4] == 'Bow' and chance[4] == 'The Ranger':
        favour = 'Thumbs down, you have been defeated'
    else:
        favour = "Goodbye"

        return Response (task, mimetype = 'text/plain')

if __name__ == '__main__':
    app.run(port=5002, debug=True, host='0.0.0.0')
        

    