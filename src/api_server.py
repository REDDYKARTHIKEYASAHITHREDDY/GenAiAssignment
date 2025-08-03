
from db_store import get_all_tournaments, insert_tournament, init_data_store

from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/tournaments', methods=['GET'])
def tournaments_route():
    sport = request.args.get('sport')
    level = request.args.get('level')
    data = get_all_tournaments()

    if sport:
        data = [d for d in data if sport.lower() in d['name'].lower()]
    if level:
        data = [d for d in data if level.lower() == d['level'].lower()]

    return jsonify(data)

@app.route('/add_tournament', methods=['POST'])
def add_tournament():
    data = request.json
    insert_tournament(data)
    return jsonify({"message": "Tournament added successfully!"}), 201

if __name__ == '__main__':
    init_data_store()

    app.run(debug=True)
