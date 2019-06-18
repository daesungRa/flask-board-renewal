from flask import render_template, flash, redirect, url_for
from flask.views import MethodView
from main.forms.account_form import SignupForm, SigninForm
from main.services.user_service import User_service

class UserView(MethodView):
    def __init__(self):
        self.account_form = [SignupForm(), SigninForm()]
        self.user_service = User_service()

    def get(self, id):
        if id is None:
            return render_template('member/signup.html', account_form=self.account_form), 200
        # return user info

    def post(self):
        # register user info
        form = SignupForm()
        if form.validate_on_submit():
            from runserver import instance_path
            create_account_result = self.user_service.create_account(instance_path, form)

            ## 분기 : 등록 성공(1, home) / 파일 저장 실패(2) / db error(3)
            if create_account_result == 1:
                flash(f'[Success] 등록 성공 ({form.email.data})', 'success')
                return redirect(url_for('index'))
            elif create_account_result == 2:
                flash(f'[Warning] 파일 업로드 실패 ({form.email.data})', 'warning')
            else:
                flash(f'[Danger] 등록 실패. 관리자에게 문의하십시오. ({form.email.data})', 'danger')

        else:
            flash(f'[Failure] Invalid Information, try again please', 'warning')

        return render_template('member/signup.html', account_form=form), 200

    def put(self):
        # modify user info
        pass

    def delete(self):
        # delete user info
        pass

class SessionView(MethodView):
    def __init__(self):
        self.account_form = [SignupForm(), SigninForm()]

    def get(self, id):
        return render_template('member/signin.html', account_form=self.account_form), 200

    def post(self):
        # sign in!
        pass

    def put(self):
        pass

    def delete(self):
        # sign out!
        pass

