import os
import nltk
import pandas as pd
from nltk.corpus import stopwords
import numpy as np
#from nltk.tokenize import word_tokenize

stop_words = set(stopwords.words('spanish'))
stop_words.add("i")
stop_words.add("ii")
stop_words.add("iii")
stop_words.add("iv")

#recibe un directorio
#retorna todos los documentos de ese directorio

def getDocsinDir(directory):
    docs=[]
    for root,directories,files in os.walk(directory+'/'):
        for f in files:
            docs.append(directory+'/'+f)
    return docs

#recibe una lista de nombres de documentos
#retorna un lista de 
def getCSVs(docs):
    data=[]
    for x in docs:
        data.append(pd.read_csv(x))
    return data

#recibe un panda.Dataframes
    #elimina todos los elementos nulos y ajusta los nombres de materias y profesores
#retorna el mismo Dataframe  
def cleanData(data):    
        data = data[data['Materia'].notna()]
        data['NRC']=data['NRC'].replace(to_replace=np.nan,value=-1)
        #data[2].dropna(inplace=True)
        data.reset_index(drop=True,inplace=True)
        bad=data.loc[lambda y: y.Materia=='Materia']
        #print(bad)
        badIndexes=bad.index.to_list()
        #print(badIndexes)
        data.reset_index(drop=True,inplace=True)
        data=data.drop(badIndexes)
        
        return data


def initData():
	pd.options.mode.chained_assignment = None  # default='warn'
	docs=getDocsinDir("filesCSV")
	data=getCSVs(docs)
	for x in range(len(data)):
		data[x]=cleanData(data[x])
		p=[x]*len(data[x])
		data[x]['Doc']=p
	
	##Recupera todas las materias con sus respectivos nrc
	materias=data[0].Materia.tolist()
	nrcs=data[0].NRC.tolist()

	for x in range(len(data)-1):
	    materias.extend(data[x+1].Materia.tolist())
	    nrcs.extend(data[x+1].NRC.tolist())

	antesMat=""
	antesNrc=0
	realMaterias=[]

	for m,n in zip(materias,nrcs):
	    ahoraMat=m
	    ahoraNrc=n
	    if(antesNrc==-1):
	        #print('aqui----'+antesMat+' '+m,n,type(n))
	        helpDic={0:antesMat+' '+m,1:n}
	        realMaterias.append(helpDic)
	        #conta1+=1
	    elif(ahoraNrc!=-1):
	        helpDic={0:m,1:n}
	        #print(m,n,type(n))
	        realMaterias.append(helpDic)
	        #conta2+=1
	    antesNrc=n
	    antesMat=m
	    #conta3+=1

	p=pd.DataFrame(realMaterias)
	p=p.rename(columns={0:'Materia',1:'NRC'})

	allSubjects=p.Materia.unique().tolist()
	return allSubjects

if __name__ == '__main__':
	lista=initData()