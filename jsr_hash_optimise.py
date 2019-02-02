x=raw_input("Enter your name:")
variable=list(x)
print(variable)
scale=[]
for i in variable:
	scale.append(ord(i))
print(scale) 
prod=1
for i in scale:
	prod=prod*i
print(prod)
blah=0
for i in scale:
	blah=blah ^ i
print(blah)  
prod=prod ** blah
print(prod)
prod=prod<<2
prod=bin(prod)
print(prod)
hexastring=str(prod)
hexastring=hexastring.lstrip("0b")
print(hexastring)
lp=len( hexastring)
print(lp)
mainset=[]
if lp>64:
	hashset=hexastring[0:64]
	extralist=hexastring[64:]
  	cj=0
    
	for i in hashset:
		for j in extralist:
			if cj == 64 :
			        break
			p = int(i) ^ int(j)
			mainset.append(p)
			cj=cj+1

if lp < 64:
	mainset=hexastring
    	kk=64-lp
	mainset=mainset+hexastring[0:kk]  
print(mainset)
print(len(mainset))
hashstring=""
st=""
for i in range(0, 64, 4):
	temp=mainset[i:i+4]
	print(temp)
	for x in temp: 
		st+= str(x)  
	hashstring+=hex(int(st,2)).replace('0x','')
	st=""
print(hashstring) 
print(len(hashstring))
 