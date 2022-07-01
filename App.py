from flask import Flask

app = Flask(__name__)

# Get Matchups 
@app.route("/", methods=['GET'])
def hello_world():
    return "<p>Hello, World!</p>"

# Post new Matchup 