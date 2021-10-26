from flask import Flask
app = Flask(__name__)
# Create route
@app.route('/')
def hello_world():
    return 'Hello World'
hello_world
