import requests as rq
import bs4
import webbrowser

def getWebPages(tema):
	#googleStringSearch="http://google.com/search?="
	#search=rq.get(googleStringSearch+tema)
	#print(search.raise_for_status())
	#html=bs4.BeautifulSoup(search.text,features="html.parser")
	html=bs4.BeautifulSoup(open("pageRes.html","r").read(),features="html.parser")
	aTags=html.select('.kCrYT a')
	pages=[]
	for x in aTags:
		pages.append(x.get('href'))
	return pages


pages=getWebPages("alimentos saludables en cuarentena")
fd=open("pageResLinks.txt","w+",encoding="utf8")
for x in pages:
	fd.write(x+"\n")
#x=0
#for p in pages:
#	page=rq.get("http://google.com"+p)
#	print(page.raise_for_status())
#	print("visited:http://google.com"+p)
#	fd=open("webPages/page"+str(x)+".html","w+",encoding="utf8")
#	fd.write(page.text)




