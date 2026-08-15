arr1=list(map(int,input("Enter the array:").split()))
arr2=list(map(int,input("Enter the array:").split()))
u=[]
for i in arr1:
    if i not in u:
        u.append(i)
for j in arr2:
    if j not in u:
        u.append(j)
print(u)