from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/api")
def get_parameters():
    param1 = request.args.get('slack_name')
    param2 = request.args.get('track')

    if param1 is None or param2 is None:
        return jsonify({"error": "Both parameters (slack_name and track) are supposed to be passed in"}), 400

    response_data = {
        "slack_name": param1,
        "track": param2,
    }

    return jsonify(response_data)


if __name__ == "__main__":
    app.run()