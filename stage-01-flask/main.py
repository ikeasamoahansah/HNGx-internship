from datetime import datetime
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
        "current_day": datetime.utcnow().strftime('%A'),
        "utc_time": datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ'),
        "track": param2,
        "github_file_url": "https://github.com/Me45y63/HNGx-internship/blob/main/stage-01-flask/main.py",
        "github_repo_url": "https://github.com/Me45y63/HNGx-internship/",
        "status_code": "200",
    }

    return jsonify(response_data)


if __name__ == "__main__":
    app.run()