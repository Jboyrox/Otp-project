
import time
timestamp = int(time.time()*1000.0)
plaintextsize=input("enter the plain text block size")
plaintextsize=int(plaintextsize)
k=input("enter the key")
s1=int(k)
ipad=54
y=int(plaintextsize/8)
for i in range(y-1):
    s1=s1^ipad
p=str(s1)
message=input("enter the message")
message=str(message)
p=p+message
p=int(p)
hs1=p%timestamp
opad=92
for i in range(y-1):
    hs1=hs1^opad
q=str(hs1)
q=q+message
q=int(q)
hs2=q%timestamp
d=input("enter the number of digits in the otp")
d=int(d)
lj=1
for i in range (d):
    lj=lj*10
otp=hs2%lj
ljr=str(otp)
yy=len(ljr)
while yy<d:
        kz=randint(0,9)
        kz=str(kz)
otp=int(ljr)
print(otp)


    

