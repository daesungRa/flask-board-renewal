from flask import render_template
from flask.views import MethodView

class BoardView(MethodView):
    def get(self, _id=None):
        print('[GET] call board view function!')
        return render_template('board.html'), 200