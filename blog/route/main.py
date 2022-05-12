from flask import request
from flask_restx import Namespace, Resource
import json

Main = Namespace('main')


@Main.route('/')
class MainPage(Resource):
    def get(self):
        return '<h1>메인 페이지입니다.</h1>'

    def post(self):
        data = json.loads(request.data)['data']
        return {
            'msg': '받은 데이터는 다음과 같습니다.',
            'data': data
        }
