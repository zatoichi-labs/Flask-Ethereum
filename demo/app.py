from flask import Flask, render_template
from flask_ethereum import Web3


app = Flask(__name__)
w3 = Web3(app)


@app.route('/')
def index():
    return render_template('index.html', web3=w3)


if __name__ == '__main__':
    app.run(debug=True)
