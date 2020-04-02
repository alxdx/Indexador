from flask import Flask, request, render_template, jsonify, make_response
import indexer

app=Flask(__name__)
dictMaterias={}

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/subject')
def autoCompleteSubject():
	#searchTerm=request.get_json(force=True)-- esta parte se usa para el metodo post

	#codigo de busqueda aqui
	#termina codigo de busqueda
	res=make_response(jsonify(dictMaterias),200)
	print(res)
	return res


if __name__=='__main__':
	listaMaterias=indexer.initData()
	noneIterator=[None]*len(listaMaterias)
	dictMaterias=dict(zip(listaMaterias,noneIterator))
	app.run(debug=True)
