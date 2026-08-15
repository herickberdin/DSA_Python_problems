s=input("Enter a string:")
f={}
mc=0
m=""
for i in s:
    if i in f:
        f[i]+=1
    else:
        f[i]=1
for i in f:
    if f[i]>mc:
        mc=f[i]
        m=i
print("The most frequent char is:",m)
print("count:",mc)