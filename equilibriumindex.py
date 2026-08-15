arr=list(map(int,input("Enter the array:").split()))
for i in range(len(arr)):
    l=0
    r=0
    for j in range(i):
        l+=arr[j]
    for j in range(i+1,len(arr)):
        r+=arr[j]
    if l==r:
        print("The Equlibrium index is:",i)
        break
else:
    print("No Equilbrium index")