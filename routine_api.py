from flask import Flask, request, jsonify

app = Flask(__name__)
routines = {}

@app.route("/api/routines", methods=["GET"])
def get_routines():
    return jsonify(routines)

@app.route("/api/routines/<string:routine_name>", methods=["GET"])
def get_routine(routine_name):
    if routine_name in routines:
        return jsonify(routines[routine_name])
    else:
        return jsonify({"error": "Routine not found"}), 404

@app.route("/api/routines", methods=["POST"])
def create_routine():
    data = request.get_json()
    routine_name = data["name"]
    routines[routine_name] = data
    return jsonify({"message": "Routine created"}), 201

@app.route("/api/routines/<string:routine_name>", methods=["PUT"])
def update_routine(routine_name):
    data = request.get_json()
    if routine_name in routines:
        routines[routine_name].update(data)
        return jsonify({"message": "Routine updated"})
    else:
        return jsonify({"error": "Routine not found"}), 404

@app.route("/api/routines/<string:routine_name>", methods=["DELETE"])
def delete_routine(routine_name):
    if routine_name in routines:
        del routines[routine_name]
        return jsonify({"message": "Routine deleted"})
    else:
        return jsonify({"error": "Routine not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)