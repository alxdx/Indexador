import json
def load_materias(carrera,plan):
	try:
		fp=open("nombres_materias/"+carrera+"-"+plan+".json")
	except (FileNotFoundError,TypeError) as e:
		return {"Error":"Horarios no encontrados"}

	return json.load(fp)
		