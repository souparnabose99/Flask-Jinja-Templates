from flask import render_template


def index():
    return "Welcome to Home Page"

def index_tem(name,var):
    return render_template('index.html',name=name,var=var)

def index_for():
    data = {'Name':'Souparna','Age':25,'Sex':'Male'}
    return render_template('index_for.html',data=data)
