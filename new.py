n=int(input())
arr=[]
for i in range(n):
    s=input().lower()
    arr.append(s)
c=0
for i in arr:
    mc=arr.count(s)
    if mc>c:
        c=mc
print(c)

