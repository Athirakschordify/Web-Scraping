from flask import Flask

# Create an instance of the Flask class
app = Flask(__name__)

# Define a route and the corresponding function
@app.route('/')
def index():
    return 'Hello, World!'

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
