arr=list(map(int,input("Enter the array:").split()))
flag=True
for i in range(len(arr)-1):
    if arr[i]>arr[i+1]:
        flag=False
        break
if flag:
    print("Sorted")
else:
    print("Not sorted")