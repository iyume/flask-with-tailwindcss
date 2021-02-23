import httpx

from flask import Blueprint, render_template, redirect, url_for, request


tiku_paper = Blueprint('tiku_paper', __name__)
# prefix '/tiku/paper'

@tiku_paper.route('/1', methods=['GET'])
def route1():
    type = request.args['type'] or None
    if type == 'random':
        def fetch():
            with httpx.Client() as client:
                f = client.get('http://127.0.0.1:8000/api/v1/?type=1')
            return f.json()['result']
        question = fetch()
        if isinstance(question, dict) and 'q' in question:
            return render_template('tiku/paper/基金基础.html', question=question)
        else:
            return render_template('tiku/paper/基金基础.html', question=0)
    else:
        return redirect(url_for('tiku_area.index'))
