from flask import Flask

# Create the Flask application instance
app = Flask(__name__)

# Route for the homepage
@app.route('/')
def home():
    return 'Hello, Flask!'

# Route for the about page
@app.route('/about')
def about():
    return 'This is my first Flask app!'

# Run the app in debug mode (auto-reloads on save, shows detailed errors)
if __name__ == '__main__':
    app.run(debug=True)