import re 
import requests 
s=[] 
sx=[]
str1='http://www.mosigra.ru/'
response = requests.get(str1) 
a=re.findall(r'(\w*@\w*[.]\w*)',str(response.content)) 
a=set(a) 
i=1
for word in a:
	s.insert(i,word)
	i=i+1 
j=1
b=re.findall(r'http:\/\/www\.mosigra\.ru\/[\w\d:#@%\/;$~_?\+-=\/\.&]*',str(response.content)) 
b=set(b)
for word in b:
	sx.insert(j,word)
	j=j+1 
k=1
while k<9:
	b=re.findall(r'http|https:\/\/\w*\.\w*\.\w*\/[\w\d:#@%\/;$~_?\+-=\/\.&]*',str(response.content)) 
	b=set(b)
	for word in b:
		if str1.rfind(word)!=-1:
			sx.insert(j,word)
			j=j+1 
	response = requests.get(sx[k]) 
	a=re.findall(r'(\A[^@]+@([^@\.]+\.)+[^@\.]+\z)',str(response.content)) 
	a=set(a) 
	i=1
	for word in a:
		t=0
		for n in range(1,i):
			if word==sx[n]:
				t=1
		if t==0:
			s.insert(i,word)
			i=i+1 
	k=k+1
s=set(s)
print(s)