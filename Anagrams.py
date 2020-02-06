t=int(input())
for i in range(t):
    counter=0
    a=list(map(str,input()))
    b=list(map(str,input()))
    orig=len(a+b)
    print(orig)
    p,q=len(a)-1,len(b)-1
    while(p>=0):
        k=a[p]
        if a[p] not in b:
            
            a.pop(p)
        p-=1

    while(q>=0):        
        k=a[p]
        if b[q] not in a:
            
            b.pop(q)

        q-=1

    
    print(len(a))
    print(len(b))
    print("\n")      
    print(orig-2*((len(a),len(b))[len(a)>len(b)]))