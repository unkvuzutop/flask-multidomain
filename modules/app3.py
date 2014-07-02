from flask import Blueprint

app3 = Blueprint('app3', __name__,
                        template_folder='templates/app3', url_prefix='/app3')

@app3.route('/')
def index():
    return 'app3.index'