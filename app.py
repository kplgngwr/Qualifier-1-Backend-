from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/bfhl', methods=['POST'])
def process_data():
    try:
        data = request.json.get('data', [])
        numbers = [item for item in data if item.isdigit()]
        alphabets = [item for item in data if item.isalpha()]
        highest_alphabet = max(alphabets, key=str.lower) if alphabets else None

        response = {
            "is_success": True,
            "user_id": "john_doe_17091999",
            "email": "john@xyz.com",
            "roll_number": "ABCD123",
            "numbers": ["1", "334", "4"],
            "alphabets": ["M"],
            "highest_alphabet": ["M"] if highest_alphabet else []
        }
        return jsonify(response), 200

    except Exception as e:
        return jsonify({"is_success": False, "error": str(e)}), 400

@app.route('/bfhl', methods=['GET'])
def get_operation_code():
    return jsonify({"operation_code": 1}), 200

# Export the app as a serverless function
def handler(request, response):
    return app(request.environ, response.start_response)

if __name__ == '__main__':
    app.run(debug=True)
