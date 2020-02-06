path=list(map(str,input()))
location=[0,0]
for i in path:
    if i=='L':
        location[0]-=1
    elif i=='R':
        location[0]+=1
    elif i=='U':
        location[1]+=1
    elif i=='D':
        location[1]-=1
print(str(location[0]),' ',str(location[1]))