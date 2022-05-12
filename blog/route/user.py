from flask import request
from flask_restx import Namespace, Resource
import json

User = Namespace('user')


@User.route('/')
class MainPage(Resource):
    def get(self):
        return '<h1>회원 페이지입니다.</h1>'

    def post(self):
        user_data = json.loads(request.data)['user']
        return {
            'msg': '받은 데이터는 다음과 같습니다.',
            'data': user_data
        }


@User.route('/<string:name>')
class MainPage(Resource):
    def get(self, name):
        return f'<h1>회원 {name}의 페이지입니다.</h1>'

    def post(self):
        user_data = json.loads(request.data)['user']
        return {
            'msg': '받은 데이터는 다음과 같습니다.',
            'data': user_data
        }
