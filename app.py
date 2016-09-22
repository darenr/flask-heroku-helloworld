#!/usr/bin/env python
# -*- coding: utf-8 -*--

from flask import Flask, render_template, request, Response, jsonify, redirect, abort, current_app
from functools import wraps
from flask_compress import Compress
import urllib3
import json
import os
import traceback
import flask_login as flask_login # only needed to support login accounts
from flask_cors import CORS

urllib3.disable_warnings()

app = Flask(__name__)
Compress(app)
CORS(app)

def mk_json_response(results={}, error_message=None):
    j = {
        'results': results,
        'status': 'OK' if not error_message else error_message
    }
    return Response(json.dumps(j, ensure_ascii=False, indent=2, encoding='utf-8'),  mimetype='application/json; charset=utf-8')


#
#
# An example of a web page, the html is found in tmplates/
#
# Static content is referred to in templates with /static/<whatecver>
# which maps to the static folder
#

@app.route('/', methods=['GET'])
def homepage():
    try:
        return render_template("index.html")

    except Exception, e:
        traceback.print_exc()
        return str(e)


#
#
# An example of a JSON REST api 
#
# test with http://localhost:5000/api/hello
#
@app.route('/api/hello', methods=['GET'])
def example_json_api():
    return mk_json_response(results={
        "say": "hello world"
    })

print ' * Ready...'

if __name__ == "__main__":

    app.run(debug=True, host='0.0.0.0', threaded=True,
            processes=1, port=5000, passthrough_errors=True)
