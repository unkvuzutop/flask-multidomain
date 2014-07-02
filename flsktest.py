import random
from flask import Flask, url_for
from flask.ext.sqlalchemy import SQLAlchemy

from modules import app1, app2, app3

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.db'
db = SQLAlchemy(app)

db.create_all()


def domain_url_for(domain_type, endpoint, **values):
    from models import ModelDomain

    values['_external'] = False
    url = url_for('%s.%s' % (domain_type, endpoint), **values)

    domains = ModelDomain.query.filter_by(domain_type=domain_type).all()
    if domains:
        random.seed()
        domain = random.choice(domains)
        return 'http://%s%s' % (domain.domain, url[len(domain_type) + 1:])

    return None

    # domain
    # url_for(app)


class Middleware(object):
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        from models import ModelDomain
        domain = ModelDomain.query.filter_by(domain=environ['HTTP_HOST'].lower()).first()
        if domain:

            environ['PATH_INFO'] = '/%s%s' % (domain.domain_type, environ['PATH_INFO'])
        return self.app(environ, start_response)


app.wsgi_app = Middleware(app.wsgi_app)

for md in [app1.app1, app2.app2, app3.app3]:
    app.register_blueprint(md)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
