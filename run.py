# coding: utf8
#!flask/bin/python
from app import app

def app(environ, start_response):
    data = "Hello, World!\n"
    start_response("200 OK", [("Content-Type", "text/html"), ("Content-Length", str(len(data)))])
    app.run(debug = True)
    return iter([data])