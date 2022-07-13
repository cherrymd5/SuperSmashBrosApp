from flask import Flask, request
from flask import jsonify
from db_connection import get_matches, write_match
import requests


app = Flask(__name__)

# Get Matchups 
@app.route("/", methods=['GET'])
def hello_world():
    return "Hello, World! Whooo"

@app.route("/get-all-matches", methods=['GET'])
def get_all_matches():
    # print(get_matches()[0][0])
    response = get_matches() # [1, 5, 23, 53, [0, 2, 5]] --> index starts at 0
    print(response[0][1])

    result = []
    for row in response: 
        data = {
            "player": row[3],
            "opponent": row[4],
            "result": row[5]
        }
        result.append(data)

    return jsonify(result)

    # json = javascript object notation 

# Post new Matchup 
@app.route("/put-match", methods=['PUT'])
def put_match():
    player = request.args.get('player')
    opponent = request.args.get('opponent')
    result = request.args.get('result')

    print("{} {} {}".format(player, opponent, result))

    write_match(player, opponent, result)

    # print(request.args.get('player'))
    return 'match posted'



# DRY - Do not repeat