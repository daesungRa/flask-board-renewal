from flask import render_template
from main import db, create_app
from main.routes import register_api, index, autocomplete, user, board

app = create_app()
reg = register_api.Register_api(app)

reg.register_api(index.IndexView, 'index', '/')
reg.register_api(index.ContactView, 'contact', '/contact/')
reg.register_api(autocomplete.AutocompleteView, 'autocomplete', '/autocomplete/')
reg.register_api(autocomplete.AutocompleteSearchView, 'search', '/search/')

reg.register_api(user.UserView, 'user', '/users/', pk='email', pk_type='string')

reg.register_api(board.BoardView, 'board', '/boards/', pk='_id', pk_type='string')

# error routes
@app.errorhandler(404)
def page_not_found(error):
    app.logger.error(error)
    return render_template('error/404.html'), 200

@app.errorhandler(500)
def server_side_error(error):
    app.logger.error(error)
    return render_template('error/500.html'), 200

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)