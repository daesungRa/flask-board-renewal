from main import db, create_app
from main.routes import register_api, index, user, board

app = create_app()
reg = register_api.Register_api(app)

reg.register_api(index.IndexView, 'index', '/')
reg.register_api(user.UserView, 'user', '/users/', pk='email', pk_type='string')
reg.register_api(board.BoardView, 'board', '/boards/', pk='_id', pk_type='string')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)