# coding: utf8
#!flask/bin/python

def app(environ, start_response):
    from app import app
    data = "Hello, World!\n"
    start_response("200 OK", [("Content-Type", "text/html"), ("Content-Length", str(len(data)))])
    app.run(debug = True)
    return iter([data])