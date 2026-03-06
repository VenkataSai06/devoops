from flask import Flask

# Create Flask app
app = Flask(__name__)

# Route for home page
@app.route('/')
def home():
    return "Hello, this is my first Flask route!"

# Route for about page
@app.route('/about')
def about():
    return "This is the About page."

# Run the application
if __name__ == '__main__':
    app.run(debug=True)