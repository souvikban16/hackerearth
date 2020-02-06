def tostr(s):
    st=''
    for i in s:
        st=st+i
    return st

s=list(map(str,input()))
for i in range(len(s)):
    if s[i].isupper():
        s[i]=s[i].lower()
    else:
        s[i]=s[i].upper()

print(tostr(s))