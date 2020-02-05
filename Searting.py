t=int(input())
for i in range(t):
    WS1=[];WS2=[]
    MS1=[];MS2=[]
    AS1=[];AS2=[]
    i=1
    while(i<=108):
        WS1.append(i);i+=1
        MS1.append(i);i+=1
        AS1.append(i);i+=1
        AS2.append(i);i+=1
        MS2.append(i);i+=1
        WS2.append(i);i+=1
        WS2.append(i);i+=1
        MS2.append(i);i+=1
        AS2.append(i);i+=1
        AS1.append(i);i+=1
        MS1.append(i);i+=1
        WS1.append(i);i+=1
    search = int(input())
    if search in WS1:
        if WS1.index(search)%2!=0:
            print(str(WS1[WS1.index(search)-1])+" WS")
        else:
            print(str(WS1[WS1.index(search)+1])+" WS")

    elif search in WS2:
        if WS2.index(search)%2!=0:
            print(str(WS2[WS2.index(search)-1])+" WS")
        else:
            print(str(WS2[WS2.index(search)+1])+" WS")

    elif search in MS1:
        if MS1.index(search)%2!=0:
            print(str(MS1[MS1.index(search)-1])+" MS")
        else:
            print(str(MS1[MS1.index(search)+1])+" MS")
    elif search in MS2:
        if MS2.index(search)%2!=0:
            print(str(MS2[MS2.index(search)-1])+" MS")
        else:
            print(str(MS2[MS2.index(search)+1])+" MS")
    elif search in AS1:
        if AS1.index(search)%2!=0:
            print(str(AS1[AS1.index(search)-1])+" AS")
        else:
            print(str(AS1[AS1.index(search)+1])+" AS")
    elif search in AS2:
        if AS2.index(search)%2!=0:
            print(str(AS2[AS2.index(search)-1])+" AS")
        else:
            print(str(AS2[AS2.index(search)+1])+" AS")