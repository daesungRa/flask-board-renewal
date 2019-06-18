from flask import render_template, g
from flask.views import MethodView
from main.forms.account_form import SignupForm, SigninForm

class UserView(MethodView):
    def __init__(self):
        account_form = [SignupForm(), SigninForm()]
        g.account_form = account_form

    def get(self, email=None):
        print('[GET] call user view function!')
        return render_template('user.html'), 200