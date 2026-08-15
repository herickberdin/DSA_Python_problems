s=input("Enter a string:")
res=""
c=1
for i in range(1,len(s)):
    if s[i-1]==s[i]:
        c+=1
    else:
        res+=s[i-1]+str(c)
        c=1
res+=s[-1]+str(c)
print(res)