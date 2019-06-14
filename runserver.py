from main import db, create_app
from main.routes import index, user, board

# 각 as_view 함수의 첫 번재 인자로 투입되는 문자열에 해당하는 "view function" 이 생성된다.
# 기존 클래스가 가지고 있던 function 자체로서는 진정한 의미의 view function 은 아니다.
# 진정한 view function 이 되려면 "dispatch_request" 함수의 구현과 함께 reverse-lookup 을 위한 "end-point" 가 성립이 되어야 하는데,
# 이를 위해 "flask.views.View" 혹은 restful api 를 위한 "flask.views.MethodView" 를 구현한 클래스가 필요한 것이다.
# 사실 아래에서 사용한 *View 클래스들은 이것의 구현체이며,
# as_view 함수 호출 시 생성자에 의해 self.template_name 이 정의된다.
# 이후 부모 클래스의 dispatch_request 함수가 자동으로 호출되면서 실제 view function 의 내용으로 사용될 자손 클래스의 함수를 탐색한다.
indexView = index.IndexView.as_view('home', template_name='home.html')
userView = user.UserView.as_view('user', template_name='user.html')
boardView = board.BoardView.as_view('board', template_name='board.html')

app = create_app()
app.add_url_rule('/', view_func=indexView)
app.add_url_rule('/user', view_func=userView)
app.add_url_rule('/board', view_func=boardView)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)