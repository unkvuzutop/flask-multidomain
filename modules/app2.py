from flask import Blueprint

app2 = Blueprint('app2', __name__,
                        template_folder='templates/app2', url_prefix='/app2')

@app2.route('/zindex')
def index():
    return 'app2.index'
