class Register_api(object):
    def __init__(self, app):
        self.app = app

    def register_api(self, view, endpoint, url, uri='', pk='id', pk_type='int'):
        view_func = view.as_view(endpoint)
        self.app.add_url_rule(url, defaults={pk: None}, view_func=view_func, methods=['GET',])
        self.app.add_url_rule(url, view_func=view_func, methods=['POST',])
        self.app.add_url_rule('%s<%s:%s>' % (url, pk_type, pk), view_func=view_func, methods=['GET', 'PUT', 'DELETE',])
        if uri is not '':
            self.app.add_url_rule(url+uri, defaults={pk: None}, view_func=view_func, methods=['GET',])
            self.app.add_url_rule('%s%s/<%s:%s>' % (url, uri, pk_type, pk), view_func=view_func, methods=['GET', 'PUT', 'DELETE', ])
