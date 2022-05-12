from blog import create_app

app = create_app()

if __name__ == '__main__':
    print(__name__)
    app.run(debug=True)


'''
__init__.py 파일을 blog 폴더 내에 생성했으므로 blog는 파이썬 패키지가 된다!!
따라서 from blog 이렇게 폴더 이름으로부터 __init__.py에 정의한 모든 것을 import
할 수 있게 된다. (create_app과 같이)

'''
