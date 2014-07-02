from flask import Flask, url_for, Blueprint
from flask.ctx import RequestContext
from werkzeug.exceptions import HTTPException
from werkzeug.routing import Map
from modules import domain_1
from modules import domain_2

from werkzeug.wsgi import DispatcherMiddleware
from modules import domain_3

class ExRequestContext(RequestContext):
    def match_request(self):
        """Can be overridden by a subclass to hook into the matching
        of the request.
        """
        try:
            url_rule, self.request.view_args = \
                self.url_adapter.match(return_rule=True)
            self.request.url_rule = url_rule
        except HTTPException as e:
            self.request.routing_exception = e

class ExFlask(Flask):
    def request_context(self, environ):
        return RequestContext(self, environ)

class ExMap(Map):
    def bind_to_environ(self, environ, **kwargs):
        return super(ExMap, self).bind_to_environ(environ, **kwargs)

app = ExFlask(__name__)


app.url_map = ExMap()
app.register_blueprint(domain_1.app1)
app.register_blueprint(domain_2.app2)


class Middleware(object):
    def __init__(self, app):
        self.app = app
    def __call__(self, environ, start_response):
        environ['PATH_INFO'] = '/app1%s' % environ['PATH_INFO']
        return self.app(environ, start_response)


from werkzeug.routing import BaseConverter, AnyConverter, Map


class ListConverter(AnyConverter):
    def to_python(self, value):
        return value.split(',')
    def to_url(self, values):

        return AnyConverter.to_url(values)


app.wsgi_app = Middleware(app.wsgi_app)
app.url_map.converters['any'] = ListConverter

from database import db_session

def custom_url_for(endpoint, **values):
    url = url_for(endpoint, **values)

    return 'http://mdm.ru/%s' % url


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()



@app.errorhandler(404)
def page_not_found(e):
    return 'jopa', 404

@app.route('/')
def index():
    print custom_url_for('index')
    return 'Hello World!'

if __name__ == '__main__':
    app.run(debug=True, port=5000)
