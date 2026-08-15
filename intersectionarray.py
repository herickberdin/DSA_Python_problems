arr=list(map(int,input("Enter the first array:").split()))
arr2=list(map(int,input("Enter the second array:").split()))
for i in arr:
    if i in arr2:
        print(i)