from flask import Blueprint, render_template

app3 = Blueprint('app3', __name__,
                        template_folder='templates', url_prefix='/app3')

@app3.route('/')
def index():
    return render_template('app3/index.html')

@app3.route('/another-link/')
def another():
    return 'another'