from flask import Flask, url_for, Blueprint
from flask.ctx import RequestContext
from werkzeug.exceptions import HTTPException
from modules import app1, app2, app3

app = Flask(__name__)

class Middleware(object):
    def __init__(self, app):
        self.app = app
    def __call__(self, environ, start_response):
        environ['PATH_INFO'] = '/app1%s' % environ['PATH_INFO']
        return self.app(environ, start_response)


app.wsgi_app = Middleware(app.wsgi_app)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
