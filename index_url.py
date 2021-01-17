from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "This is the homepage"

#variable rules
@app.route('/<name>')
def varibale(name):
    return "this is the variable {}".format(name)


@app.route('/blog/<int:blogid>')
def blog(blogid):
    return "This is the blog value {}".format(blogid)

@app.route('/weight/<float:w>')
def weight(w):
    return "Weight is %s"%w


if __name__ == '__main__':
    app.run(debug=True)