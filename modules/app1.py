from flask import Blueprint, render_template, url_for, _app_ctx_stack, _request_ctx_stack
from werkzeug.routing import BuildError
from werkzeug.urls import url_quote

app1 = Blueprint('app1', __name__,
                        template_folder='templates/app1', url_prefix='/app1')


@app1.route('/')
def index():
    return render_template('index.html')

