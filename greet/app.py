from flask import Flask, request


#makes new server 
app = Flask(__name__)
if __name__ == '__main__':
    app.run(debug=True)


@app.route('/welcome')
def welcome():
    return "welcome"

@app.route('/welcome/home')
def welcome_home():
    return "welcome home"

@app.route('/welcome/back')
def welcome_back():
    return "welcome back"

