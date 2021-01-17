from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to Flask"

@app.route('/route1')
def route():
    return "This is route1"

def route2():
    return 'This is route2'

app.add_url_rule('/route2','route2',route2)

if __name__ == "__main__":
    app.run(host='127.0.0.1',port=8000,debug=True)