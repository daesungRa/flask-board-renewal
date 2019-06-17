from flask import render_template
from flask.views import MethodView

class UserView(MethodView):
    def get(self, email=None):
        print('[GET] call user view function!')
        return render_template('user.html'), 200