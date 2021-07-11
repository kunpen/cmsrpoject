from flask import Blueprint

bp=Blueprint("admin",__name__)
@bp.route('/admin')
def index():
    return '这里是后台首页'