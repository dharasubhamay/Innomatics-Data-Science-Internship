#Step 1 - import Flask
from flask import Flask, render_template, request
import re

#Step 2 - Create Object
app = Flask(__name__)

#Step 3 - Adding Functionality
@app.route('/')
def home_page():
    if request.method == 'GET':
        return render_template('regex.html')

@app.route('/search', methods=['GET', 'POST'])
def search_regex():
    exp = request.form.get('exp')
    txt = request.form.get('txt')
    r = re.findall(exp, txt)
    res = ""
    for i in r:
        res = res + ' ' + i
    return res

#Step 4 - Run the app
if __name__ == "__main__":
    app.run()