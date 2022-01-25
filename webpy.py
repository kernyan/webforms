#! /usr/bin/env python3

from flask import Flask, render_template, request
import base64

app = Flask(__name__)

def to_svg(image):
    return base64.b64encode(image.encode('utf-8')).decode('utf-8')

@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        r0 = request.form['r0']
        r1 = request.form['r1']
        r2 = request.form['r2']
        r3 = request.form['r3']

    imgtemp = '<img width=600 height=600 src="data:image/svg+xml;base64,%s"></img><br/>'
    s = open('circle.svg', 'r').read()
    imageV = {}
    imageV['image1'] = imgtemp % to_svg(s)
    return render_template('index.html', imgf=imageV)

if __name__ == '__main__':
    app.run()
