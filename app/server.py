from flask import render_template, request
from app import app

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        pass


@app.route('/about/')
def about():
    return render_template('about.html')
