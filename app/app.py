from flask import Flask, render_template, redirect, url_for

from app.tiku.area import tiku_area
from app.tiku.paper import tiku_paper


app = Flask(__name__)

app.register_blueprint(tiku_area, url_prefix='/tiku/area')
app.register_blueprint(tiku_paper, url_prefix='/tiku/paper')

@app.route('/')
def index():
    return redirect(url_for('tiku_area.index'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@app.route('/user')
def userpage():
    return render_template('user/index.html')


@app.errorhandler(403)
def forbidden(error):
    return 'Forbidden 403', 403

@app.errorhandler(404)
def page_not_found(error):
    return 'Page Not Found 404', 404

@app.errorhandler(500)
def internal_server_error(error):
    return 'Webserver Error', 500

