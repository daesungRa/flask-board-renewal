from flask import render_template, session
from flask.views import MethodView

class IndexView(MethodView):
    def get(self, id=None):
        session.permanent = True
        return render_template('index.html'), 200

class ContactView(MethodView):
    def get(self, id=None):
        return render_template('contact.html'), 200

