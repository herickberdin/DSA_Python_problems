arr=list(map(int,input("Enter the array:").split()))
f=arr[0]
for i in range(len(arr)-1):
    arr[i]=arr[i+1]
arr[-1]=f
print(arr)