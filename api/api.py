from flask import Flask,request
from flask_restful import Resource, Api
import json
import tools

app = Flask(__name__)
api = Api(app)

class Test(Resource):
    def get(self, name):
        return {"Hello":name+" puto"}

class ListaMaterias(Resource):
	def get(self):
		carrera=request.args.get("carrera","com")
		plan=request.args.get("plan","6")
		materias=tools.load_materias(carrera,plan)
		return materias

api.add_resource(Test, '/test/<name>')
api.add_resource(ListaMaterias,'/lista/')
if __name__ == '__main__':	
	app.run(debug=True)