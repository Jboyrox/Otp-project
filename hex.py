#convert string to hex
def toHex(s):
    lst = []
    for ch in s:
        hv = hex(ord(ch)).replace('0x', '')
        if len(hv) == 1:
            hv = '0'+hv
        lst.append(hv)
    
    return reduce(lambda x,y:x+y, lst)



print toHex("sanjay")
tohex = lambda x:"".join([hex(ord(c))[2:].zfill(2) for c in x])
print tohex
c="raju"
print hex(199)