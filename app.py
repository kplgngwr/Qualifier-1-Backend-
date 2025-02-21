# filepath: /c:/Users/Acer/Desktop/React Projects/Qualifier 1/my-backend-app/app.py
from flask import Flask, request, jsonify
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)

    @app.route('/')
    def health_check():
        return jsonify({"status": "healthy"}), 200

    @app.route('/api/bfhl', methods=['POST'])
    def process_data():
        try:
            # Get data from request and ensure it's a list
            data = request.json.get('data', [])
            if not isinstance(data, list):
                raise ValueError("Input 'data' must be an array")

            # Convert all items to strings and strip whitespace
            data = [str(item).strip() for item in data]

            # Filter numbers and alphabets
            numbers = [item for item in data if item.isdigit()]
            alphabets = [item for item in data if len(item) == 1 and item.isalpha()]

            # Find highest alphabet (case insensitive)
            highest_alphabet = []
            if alphabets:
                # Sort alphabets case-insensitively and take the last one
                sorted_alphabets = sorted(alphabets, key=str.lower)
                highest_alphabet = [sorted_alphabets[-1]]

            response = {
                "is_success": True,
                "user_id": "john_doe_17091999",
                "email": "john@xyz.com",
                "roll_number": "ABCD123",
                "numbers": numbers,
                "alphabets": alphabets,
                "highest_alphabet": highest_alphabet
            }
            return jsonify(response), 200

        except Exception as e:
            return jsonify({
                "is_success": False,
                "error": str(e)
            }), 400

    @app.route('/api/bfhl', methods=['GET'])
    def get_operation_code():
        return jsonify({"operation_code": 1}), 200

    # Error handling
    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({"error": "Internal Server Error"}), 500

    @app.errorhandler(404)
    def not_found_error(error):
        return jsonify({"error": "Not Found"}), 404

    return app