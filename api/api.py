from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Test(Resource):
    def get(self, name):
        return {"Hello":name+" puto"}


api.add_resource(Test, '/test/<name>')

if __name__ == '__main__':
 app.run(debug=True)