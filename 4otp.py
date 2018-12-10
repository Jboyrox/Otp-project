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
s2=s1/c2;
while check == True :
	f=0
	
	while(f!=1):
		
		otp=int(s2%random.randint(c1,c2))
		if((otp>c1)&(otp<c2)):
			f=1;
	a=int(a)^otp
	a=int(a)
	f=0
	while(f!=1):
		if((a>c1)&(a<c2)):
			f=1
		elif(a<c1):
			a=a|otp
		else:
			a=a&otp
			

	lis=a
	
	
	print (lis)
	for j in range(len(l)): 
		if (l[j]==lis):
			check=False
			break
	l.append(lis)
	c+=1
	
	a=a/10+(a%10)*c1
	
print(l)
print( "effective otp:",c)


