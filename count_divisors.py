l,r,k=input().split();
l,r,k=int(l),int(r),int(k)
counter=0
for i in range (l-1,r):
	if i%k==0:
		counter+=1
print(counter)