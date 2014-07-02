from flask import Blueprint, render_template

app2 = Blueprint('app2', __name__,
                        template_folder='templates', url_prefix='/app2')

@app2.route('/')
def index():
    return render_template('app2/index.html')
