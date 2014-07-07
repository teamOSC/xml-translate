#!/usr/bin/env python
# -*- coding: utf-8 -*-

import flask, flask.views
app = flask.Flask(__name__)

from flask import render_template,request,make_response
import json,urllib2
from bs4 import BeautifulSoup

app.config['ALLOWED_EXTENSIONS'] = set(['xml','txt'])

@app.route('/')
def index():
    return flask.render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    xml_file = request.files['upload_xml']
    xml_text = xml_file.read()
    soup = BeautifulSoup(xml_text,'xml')
    arr = []
    for item in soup.findAll():
        d = {}
        d['name'] = item.name
        d['text'] = item.get_text().strip()
        d['attributes'] = item.attrs
        if d['text']:
            arr.append(d)

    return flask.render_template('edit.html',arr=arr,xml_text=xml_text)

@app.route('/download', methods=['POST'])
def download():
    return json.dumps(request.form)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')

