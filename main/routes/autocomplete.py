from flask import request, jsonify
from flask.views import MethodView
from main.services import autocomplete_service

class AutocompleteView(MethodView):
    def __init__(self):
        self.auto_service = autocomplete_service.Autocomplete_service()

    def post(self, id=None):
        query = request.form['query']
        result = self.auto_service.find({'Name': {'$regex': query, '$options': 'i'}})
        print(result)

        return jsonify({'suggestions': result})

class AutocompleteSearchView(MethodView):
    def __init__(self):
        self.auto_service = autocomplete_service.Autocomplete_service()

    def post(self, id=None):
        word = request.values.get('word')
        result = self.auto_service.find_one({'Name': {'$regex': word, '$options': 'i'}})
        print(result)

        return jsonify({'result': result})
