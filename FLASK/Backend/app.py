from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/api/data', methods=['POST'])
def receive_data():
    data = request.json  # Extract JSON data from request
    # Process the data as needed
    # Example: You might store the data in a database
    response_data = {'message': 'Data received successfully'}  # Prepare response
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask app
