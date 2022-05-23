from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/post/chance', methods=['POST'])
def post_chance():
    generate = request.data.decode('utf-8')
    favour= generate.split()
    print(favour)
    if favour[0] == 'Claymore' and int(favour[1]) > 3:
        chance = 'Thumbs up, you survived'
    elif favour[0] == 'Fists' and int(favour[1]) > 9:
        chance = 'Thumbs up, you survived'
    elif favour[0] == 'Spear' and int(favour[1]) > 3:
        chance = 'Thumbs up, you survived'
    elif favour[0] == 'Flail' and int(favour[1]) > 6:
        chance = 'Thumbs up, you survived'
    elif favour[0] == 'Bow' and int(favour[1]) > 0:
        chance = 'Thumbs up, you survived'
    else:
        chance = "Thumbs down, you have perished"

    return Response (chance, mimetype = 'text/plain')

if __name__ == '__main__':
    app.run(port=5002, debug=True, host='0.0.0.0')
        

    