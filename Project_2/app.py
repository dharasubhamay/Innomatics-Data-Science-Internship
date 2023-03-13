#Step 1 - import Flask
from flask import Flask, request

#Step 2 - Create Object
app = Flask(__name__)

#Step 3 - Adding Functionality
@app.route('/')
def home_page():
    return "Welcome to Home Page"

@app.route('/add')
def add_fun():
    a = request.args.get('a')
    b = request.args.get('b')
    return str(int(a) + int(b))

@app.route('/upper')
def make_uppercase():
    username = request.args.get('username')
    upper_username = username.upper()
    return upper_username

#Step 4 - Run the app
if __name__ == "__main__":
    app.run()