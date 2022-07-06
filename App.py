from flask import Flask
from flask import jsonify
from db_connection import get_matches

app = Flask(__name__)

# Get Matchups 
@app.route("/", methods=['GET'])
def hello_world():
    return "<p>Hello, World! Whooo</p>"

@app.route("/get-all-matches", methods=['GET'])
def get_all_matches():
    print(get_matches()[0][0])
    data = {
        "player": get_matches()[0][3],
        "opponent": get_matches()[0][4],
        "result": get_matches()[0][5]
    }
    return jsonify(data)

# Post new Matchup 
