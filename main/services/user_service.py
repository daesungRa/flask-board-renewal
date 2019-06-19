from main.factory.fileupload import Profile_Upload
from main.factory.encryption import Encryption
from main import db
from mariaapi.models.user import User
import os

class User_service(object):
    def __init__(self):
        self.profile_upload = Profile_Upload()
        self.encryption_instance = Encryption()

    def create_account(self, instance_path, form):
        ## duplicated file check and save
        savepath = self.profile_upload.upload(instance_path, form.profile.data)

        if savepath:
            user = User(form.email.data, self.encryption_instance.hash_pwd(form.pwd.data), form.username.data,
                        form.nickname.data, savepath)
            db.session.add(user)
            db.session.commit()

            print(user.id)
            if user.id > 0:
                create_account_result = 1 # success
            else:
                # remove saved file
                filename = instance_path.split('instance')[0] + savepath
                print(f'remove file name : {filename}')
                os.remove(filename)
                create_account_result = 3 # database error
        else:
            create_account_result = 2 # fail for file save

        return create_account_result

    def access_account(self, form):
        criteria = {'email': form.email.data}
        saved_result = self.db.find_one(criteria, self.collection_name, projection=['email', 'pwd', 'nickname', 'profile'])

        if saved_result:
            result = self.encryption_instance.check_pwd(saved_result['pwd'], form.pwd.data)

            if result:
                saved_result.pop('pwd')
                return saved_result
        return None

    def find_account(self, form):
        # 이메일(아이디)이 다르다면 1, 비밀번호가 다르다면 2 플래그 반환
        # 3 번 플래그는 성공(+세션에 저장할 정보), 플래그에 따라 응답 다르게
        pass

    def modify_account(self, form):
        pass

    def delete_account(self, form):
        pass

    def signin(self, form):
        pass