
'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
def hmac( key,limit,message,plaintextsize ):
    
    
    s1=int(key)
    
    
    plaintextsize=int(plaintextsize)

    
    limit=int(limit)
    
    ipad=54
    
    y=int(plaintextsize/8)
    
    for i in range(y-1):
        
        s1=s1^ipad
    
    p=str(s1)
    message=str(message)
    p=p+message
    p=int(p)
    hs1=p%limit
    opad=92
    for i in range(y-1):
        hs1=hs1^opad
    q=str(hs1)
    q=q+message
    q=int(q)
    hs2=q%limit
    return hs2;
seed=input("enter the seed value")
seed=int(seed)
key=input("enter the key")
plaintextsize=input("enter the plaintextsize")
limit=input("enter the hash limit")
d=999
seed=int(seed)
lkf=seed
while d>=0 :
    seed=lkf
    for i in range  (d):
        message=hmac(key,limit,seed,plaintextsize)
    otp=seed
    password=hmac(key,limit,seed,plaintextsize)
    print(otp)
    print(password)
    d=d-1
    