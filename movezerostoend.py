arr=list(map(int,input("Enter an array:").split()))
l=[]
m=[]
for i in range(len(arr)):
    if arr[i]==0:
        l.append(arr[i])
    else:
        m.append(arr[i])
print(m+l)
        