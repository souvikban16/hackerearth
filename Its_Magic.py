n=int(input())
arr=list(map(int,input().split()))

sorted_arr=arr[:]
sorted_arr.sort()

total_sum=0
for i in arr:
    total_sum+=i
flag=1
for i in range(len(sorted_arr)):
    sum=total_sum-sorted_arr[i]
    if sum%7==0:
        print(arr.index(sorted_arr[i]))
        flag=0
        break
if flag==1:
    print(-1)
