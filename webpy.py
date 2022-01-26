#! /usr/bin/env python3

from flask import Flask, render_template, request
import base64
from utils import plot_svg

app = Flask(__name__)
def to_svg(image):
    return base64.b64encode(image).decode('utf-8')

def parse(r0,r1,r2,r3):
    def extract3(rx):
        tokens = rx.split(',')
        try:
            if len(tokens) == 3:
                return tuple(map(float, tokens))
            return None
        except:
            return None
    config = {}
    l = locals()
    for e in range(4):
        o = extract3(l[f'r{e}'])
        if o == None:
            return None
        config[f'r{e}'] = o
    return config

@app.route('/', methods=('GET', 'POST'))
def index():
    config = None
    if request.method == 'POST':
        r0 = request.form['r0']
        r1 = request.form['r1']
        r2 = request.form['r2']
        r3 = request.form['r3']
        config = parse(r0,r1,r2,r3)
    imgtemp = '<img width=600 height=600 src="data:image/svg+xml;base64,%s"></img><br/>'
    imageV = {'image1':''}
    if config:
        s = plot_svg(config)
        imageV['image1'] = imgtemp % to_svg(s)
    return render_template('index.html', imgf=imageV)

if __name__ == '__main__':
    app.run()
