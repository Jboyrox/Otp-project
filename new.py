import random
import string
import time
import math
 
		
l=[]
c=0
s1=input("Enter your number:")
d=int(input("enter the number of digits in the otp:"))
c1=math.pow(10,d-1)
c2=math.pow(10,d)
a=int(int(time.time()%c2)&int(s1%random.randint(c1,c2)))
check=True
while check == True :
	
	

	otp=int(s1/random.randint(c1,c2))
	
	a=int(a)^otp
	a=int(a)
	
	while(1):
		
		if(a<c1):
			a*=random.randint(1,30)
		elif(a>c2):
			a=int(a/random.randint(1,30))
		else :
			break

	lis=a
	
	
	print (lis)
	for j in range(len(l)): 
		if (l[j]==lis):
			check=False
			break
	l.append(lis)
	c+=1
	
	a=a/10+(a%10)*c1+random.randint(1,30)
	
	
print(l)
print( "effective otp:",c)


