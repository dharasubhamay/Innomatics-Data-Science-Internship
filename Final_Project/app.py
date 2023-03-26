import os
from flask import Flask, redirect, request, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import random
import string

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)

class ShortenUrl(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    actualUrl = db.Column(db.String())
    shortenUrl = db.Column(db.String(15))

    def __init__(self, actualUrl, shortenUrl):
        self.actualUrl = actualUrl
        self.shortenUrl = shortenUrl
    def __repr__(self) -> str:
        return f"{self.actualUrl} - {self.shortenUrl}"

def makeShortenUrl():
    availableChars = string.ascii_lowercase + string.ascii_uppercase + string.digits
    while True:
        randomCharacters = random.choices(availableChars, k=7)
        randomCharacters = "".join(randomCharacters)
        shortenUrl = ShortenUrl.query.filter_by(shortenUrl=randomCharacters).first()
        if not shortenUrl:
            return randomCharacters

@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == "POST":
        get_url = request.form["act_url"]
        url = ShortenUrl.query.filter_by(actualUrl=get_url).first()

        if url:
            return redirect(url_for("print_short_url", url=url.shortenUrl))
        else:
            shortenUrl = makeShortenUrl()
            shortUrl = ShortenUrl(get_url, shortenUrl)
            db.session.add(shortUrl)
            db.session.commit()
            return redirect(url_for("print_short_url", url=shortUrl))
    else:
        return render_template('showShortUrl.html')
    
@app.route('/<short_url>')
def redirection(short_url):
    act_url = ShortenUrl.query.filter_by(shortenUrl=short_url).first()
    if act_url:
        return redirect(act_url.actualUrl)
    else:
        return f'<h1>Url doesnt exist</h1>'

@app.route('/print/<url>')
def print_short_url(url):
    return render_template('showShortUrl.html', short_url_print=url)

@app.route('/history')
def history():
    return render_template('history.html', vals=ShortenUrl.query.all())

@app.route('/delete/<int:id>')
def delete(id):
    url = ShortenUrl.query.filter_by(id=id).first()
    db.session.delete(url)
    db.session.commit()
    return redirect("/history")


if __name__ == '__main__':
    app.run(debug=True)