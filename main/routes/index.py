from flask import render_template
from flask.views import MethodView

class IndexView(MethodView):
    def __init__(self):
        pass

    def get(self, id=None):
        print('[GET] call index view function!')
        return render_template('home.html'), 200