import os
from flask.ext.sqlalchemy import SQLAlchemy
import flsktest
import unittest
from flask.ext.webtest import TestApp
from models import ModelDomain, db

class TestCase(unittest.TestCase):

    def setUp(self):
        # flsktest.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
        flsktest.app.config['TESTING'] = True

        self.db = db
        # db.init_app(flsktest.app)


        with flsktest.app.app_context():
            db.create_all()

        try:

            self.db.session.add(ModelDomain('host11.ru', 'app1'))
            self.db.session.add(ModelDomain('host12.ru', 'app1'))

            self.db.session.add(ModelDomain('host22.ru', 'app2'))

            self.db.session.add(ModelDomain('host31.ru', 'app1'))
            self.db.session.add(ModelDomain('host33.ru', 'app3'))

            self.db.session.commit()
        except Exception, e:
            print(e)


        self.w = TestApp(flsktest.app)

    def tearDown(self):
        self.db.session.remove()
        self.db.drop_all()

    def testDomainUrlFor(self):
        flsktest.app.config['SERVER_NAME'] = 'localhost'

        from flsktest import domain_url_for

        with flsktest.app.app_context():
            print domain_url_for('app1', 'index')
            print domain_url_for('app2', 'index')
            print domain_url_for('app3', 'index')
            print domain_url_for('app3', 'another')

        flsktest.app.config['SERVER_NAME'] = None
        # print ModelDomain.query.filter_by(domain_type='app1').first()



        # print ModelDomain.query.all()


    def testIndex(self):
        try:
            res = self.w.get('/', extra_environ = {
                'HTTP_HOST' : 'host1.ru',
                'SERVER_NAME' : 'host1.ru'
            })
            print res.body

        except Exception, e:
            print e


        print 'hos11'
        print '***' * 30
        try:
            res = self.w.get('/', extra_environ = {
                'HTTP_HOST' : 'host11.ru',
                'SERVER_NAME' : 'host11.ru'
            })

            print res.body
        except Exception, e:
            print e


        print '***' * 30
        print 'hos12'
        try:
            res = self.w.get('/', extra_environ = {
                'HTTP_HOST' : 'host12.ru',
                'SERVER_NAME' : 'host12.ru'
            })

            print res.body
        except Exception, e:
            print e

        print '***' * 30
        try:
            res = self.w.get('/', extra_environ = {
                'HTTP_HOST' : 'host22.ru',
                'SERVER_NAME' : 'host22.ru'
            })

            print res.body
        except Exception, e:
            print e

        print '***' * 30
        try:
            res = self.w.get('/', extra_environ = {
                'HTTP_HOST' : 'host31.ru',
                'SERVER_NAME' : 'host31.ru'
            })

            print res.body
        except Exception, e:
            print e

        print '***' * 30
        try:
            res = self.w.get('/', extra_environ = {
                'HTTP_HOST' : 'host33.ru',
                'SERVER_NAME' : 'host33.ru'
            })

            print res.body
        except Exception, e:
            print e

# if __name__ == '__main__':
#     unittest.main()