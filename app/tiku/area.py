from flask import Blueprint, render_template


tiku_area = Blueprint('tiku_area', __name__)
# prefix '/tiku/area'

@tiku_area.route('/', methods=['GET'])
def index():
    return render_template('tiku/area/index.html')

@tiku_area.route('/1', methods=['GET'])
def type1():
    return render_template('tiku/area/基金基础.html')

@tiku_area.route('/2', methods=['GET'])
def type2():
    return render_template('tiku/area/基金法规.html')

@tiku_area.route('/3', methods=['GET'])
def type3():
    return render_template('tiku/area/证券法规.html')
