
from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory database
events = [
    {"id": 1, "title": "Yoga in the Park"},
    {"id": 2, "title": "Lake 5K Run"}
]


# Homepage
@app.route("/", methods=["GET"])
def welcome():
    return jsonify({"message": "Welcome!"}), 200


# GET - Retrieve all events
@app.route("/events", methods=["GET"])
def get_events():
    return jsonify(events), 200


# POST - Create a new event
@app.route("/events", methods=["POST"])
def add_event():
    # Read incoming JSON data
    data = request.get_json(silent=True)

    # Validate incoming data
    if not isinstance(data, dict):
        return jsonify({"error": "Invalid JSON data"}), 400

    title = data.get("title")

    if not isinstance(title, str) or not title.strip():
        return jsonify({"error": "Event title is required"}), 400

    # Generate a new event ID
    new_id = max((e["id"] for e in events), default=0) + 1

    # Create a new event
    new_event = {
        "id": new_id,
        "title": title.strip()
    }

    # Add the event to the database
    events.append(new_event)

    # Return created event
    return jsonify(new_event), 201


if __name__ == "__main__":
    app.run(debug=True)
