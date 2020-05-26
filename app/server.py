from flask import Flask, request, render_template, jsonify, make_response
import requests

app=Flask(__name__)
dictMaterias={}

@app.route('/')
def home():
	return render_template('index.html')


@app.route('/hello/<name>')
def test(name):
	info=requests.get('http://localhost:5000/test/'+name)
	return info.text

@app.route('/subject/')
def autoCompleteSubject():
	#searchTerm=request.get_json(force=True)-- esta parte se usa para el metodo post
	carrera=request.args.get("carrera",None)
	plan=request.args.get("plan",None)
	res=requests.get('http://localhost:5000/lista/',params={"carrera":carrera,"plan":plan})
	return res.text


if __name__=='__main__':
	#p=Indexer()
	#listaMaterias=p.initData()
	#noneIterator=[None]*len(listaMaterias)
	#dictMaterias=dict(zip(listaMaterias,noneIterator))
	app.run(debug=True,port=80)

