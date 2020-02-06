def reverse(st):
    l=len(st)-1
    final=""
    while(l>=0):
        final=final+(st[l])
        l-=1
    return final

s=input()
if(s==reverse(s)):
    print("YES")
else:
    print("NO")