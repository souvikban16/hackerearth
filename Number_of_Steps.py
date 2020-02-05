n=int(input())
a=[]
b=[]

a=list(map(int,input().split()))
b=list(map(int,input().split()))
steps=0
status=0
while(1):

    for i in range(n):
        if a[i]==b[i]:
            status=1

    for i in range(n):
        if a[i]>b[i]:
            status=0
        
    for i in range(n):
        if a[i]<b[i]:
            status=-1
    if status==1:
        print(steps)
        break

    elif status==0:
        for i in range(n):
            a[i]+=-b[i]
            steps+=1
    elif status==-1:
        print(-1)
        break
