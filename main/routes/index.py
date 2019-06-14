from flask import render_template
from flask.views import MethodView
import inspect

class IndexView(MethodView):
    def __init__(self, template_name):
        self.template_name = template_name

    def get(self):
        print(inspect.stack()[1][3])
        print(inspect.stack()[2][3])
        print('[GET] call index view function!')
        return render_template(self.template_name), 200