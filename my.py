

                           
import time
import random
timestamp = int(time.time()%10000)
print(timestamp)


ipad=timestamp
z=random.randint(100,900)
y=int(z/8)
s1=int(input("Enter your number"))
hs1=int(s1)
for i in range(y-1):
    hs1=hs1^ipad
timestamp = int(time.time()/987654)
hs2=hs1%timestamp
d=int(input("enter the number of digits in the otp"))

lj=1
for i in range (d):
    lj=lj*10
otp=hs2%lj
ljr=str(otp)
yy=len(ljr)
while yy<d:
        kz=random.randint(0,9)
        kz=str(kz)
otp=int(ljr)
print(otp)


    

