import random
import string
import operator
 
def ran_gen(size,chars= string.digits):
	 
	return ''.join(random.choice(chars) for x in range(size))
l=[]
c=0

check=True
while check == True :
	lis=ran_gen(4)
	print (lis)
	for j in range(len(l)):
		if (l[j]==lis):
			check=False
	l.append(lis)	
	c+=1


print(l)
print( "effective otp:",c)

