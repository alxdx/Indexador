import os
import nltk
import pandas as pd
from nltk.corpus import stopwords
import numpy as np
#from nltk.tokenize import word_tokenize
#stop_words = set(stopwords.words('spanish'))
#stop_words.add("i")
#stop_words.add("ii")
#stop_words.add("iii")
#stop_words.add("iv")

class Indexer:

	def __init__(self):
		self.Materia=[]
		self.nombresMaterias=[]
		self.data=[]
	#recibe un directorio
	#retorna todos los documentos de ese directorio
	def getDocsinDir(self,directory):
	    docs=[]
	    for root,directories,files in os.walk(directory+'/'):
	        for f in files:
	            docs.append(directory+'/'+f)
	    return docs

	#recibe una lista de nombres de documentos
	#retorna un lista de 
	def getCSVs(self,docs):
	    data=[]
	    for x in docs:
	        data.append(pd.read_csv(x))
	    return data

	#recibe un panda.Dataframes
	    #elimina todos los elementos nulos y ajusta los nombres de materias y profesores
	#retorna el mismo Dataframe  
	def cleanData(self,data):    
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

	#recibe una lista de dataframes
		#extrae todas los nombres de las materias y los
	#retorna en un lista 
	def getCleanMaterias(self,data):
	    
	    materias=data[0].Materia.tolist()
	    nrcs=data[0].NRC.tolist()
	    numOfDoc=data[0].Doc.tolist()
	    
	    for x in range(len(data)-1):
	        materias.extend(data[x+1].Materia.tolist())
	        nrcs.extend(data[x+1].NRC.tolist())
	        numOfDoc.extend(data[x+1].Doc.tolist())
	        
	    antesMat=""
	    antesNrc=0
	    realMaterias=[]
	    for m,n,d in zip(materias,nrcs,numOfDoc):
	        ahoraMat=m
	        ahoraNrc=n
	        if(antesNrc==-1):
	            #print('aqui----'+antesMat+' '+m,n,type(n))
	            helpDic={0:antesMat+' '+m,1:n,2:str(d)}
	            realMaterias.append(helpDic)
	        elif(ahoraNrc!=-1):
	            helpDic={0:m,1:n,2:str(d)}
	            #print(m,n,type(n))
	            realMaterias.append(helpDic)
	        antesNrc=n
	        antesMat=m
	    p=pd.DataFrame(realMaterias)
	    p=p.rename(columns={0:'Materia',1:'NRC',2:'Doc'})
	    p=p.drop_duplicates()
	    return p

	def initData(self):
		pd.options.mode.chained_assignment = None  # default='warn'
		docs=self.getDocsinDir("filesCSV")
		self.data=self.getCSVs(docs)
		for x in range(len(self.data)):
			self.data[x]=self.cleanData(self.data[x])
			p=[x]*len(self.data[x])
			self.data[x]['Doc']=p
		
		##Recupera todas las materias con sus respectivos nrc
		self.Materias=self.getCleanMaterias(self.data)
		self.nombresMaterias=self.Materias.Materia.unique().tolist()
		return self.nombresMaterias
	
if __name__ == '__main__':
	p=Indexer()
	p.initData()
	print(p.data[1].head())