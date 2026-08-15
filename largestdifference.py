arr=list(map(int,input("Enter the array:").split()))
maximum=arr[1]-arr[0]
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[j]-arr[i]>maximum:
            maximum=arr[j]-arr[i]
print("The largest difference is:", maximum)