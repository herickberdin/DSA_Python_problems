arr=list(map(int,input("Enter an array:").split()))
prod=arr[0]*arr[1]
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]*arr[j]>prod:
            prod=arr[i]*arr[j]
print("The largest product is:",prod)