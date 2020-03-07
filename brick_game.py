n=int(input())

left=n
counter=1
while(left>0):
    left=left-counter
    print('remaining=',left)
    if (left<=counter*2):
        print('Patlu')
        break
    else:

        left=left-counter*2
        if(left<=counter):
            print('Motu')
    counter+=1
