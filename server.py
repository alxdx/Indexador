from flask import Flask, request, render_template, jsonify, make_response
import indexer

app=Flask(__name__)

@app.route('/')
def home():
	indexer.testing()
	return render_template('index.html')

@app.route('/subject',methods=["POST"])
def autoCompleteSubject():
	searchTerm=request.get_json(force=True)
	#codigo de busqueda aqui

	#termina codigo de busqueda
	res=make_response(jsonify({"termino1":None,"termino3":None}	),200)
	print(res)
	return res

if __name__=='__main__':
	app.run(debug=True)
