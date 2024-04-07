def cipher(text,a,b,m):
    text=text.upper()
    init=[]

    #print([*text])
    for x in [*text]:
        if x!=' ':
            #print(ord(x)-65,end=' ') #this is ASCII btw
            init.append(ord(x)-65)
        else:
            init.append(' ')
    #print(init)
    func=[]
    for i in init:
        if i!=' ':
            func.append((a*i+b)%m)
        else:
            func.append(i)
    
    ciphertext=[]
    for i in func:
        if i!=' ':
            ciphertext.append(chr(i+65))
        else:
            ciphertext.append(' ')
    
    return(("".join(ciphertext)))
    
def inverse(r1,r2):
    mod=r2
    #r2=26
    s1=1
    s2=0
    t1=0
    t2=1
    if r1<r2:
        r1,r2=r2,r1
    while(r2!=0):
        q=r1//r2
        r=r1%r2
        s=s1-s2*q
        t=t1-t2*q
        r1=r2
        r2=r
        s1=s2
        s2=s
        t1=t2
        t2=t
    if(t1<0):
        return mod+t1
    else:
        return t1

def decipher(text,a,b,m):
    text=text.upper()
    init=[]

    for x in [*text]:
        if x!=' ':
            init.append(ord(x)-65)
        else:
            init.append(' ')
    c=inverse(a,m)
    
    func=[]
    for i in init:
        if i!=' ':
            func.append(c*(i-b)%m)
        else:
            func.append(i) 
    deciphertext=[]
    for i in func:
        if i!=' ':
            deciphertext.append(chr(i+65))
        else:
            deciphertext.append(' ')
    
    return(("".join(deciphertext)))

text=input()
m=26
a=int(input())
b=int(input())
code=(cipher(text,a,b,m))
print(code)
print(decipher(code,a,b,m))
