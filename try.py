s=raw_input("Enter your data:")
d=[]
for i in s:
	print i
	d.append(ord(i))
	print hex(ord(i)).replace('0x', '')
print d
has=""
r = ""
for i in d:
    r += str(i)
r=int(r)
print r
while r >0:
	h=r%255
	r/=255
 	has+=hex(+h).replace('0x', '')
print has
