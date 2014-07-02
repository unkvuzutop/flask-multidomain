from flask import Blueprint, render_template

app1 = Blueprint('app1', __name__,
                        template_folder='templates/app1', url_prefix='/app1')

@app1.route('/')
def index():
    return render_template('app1/index.html')

