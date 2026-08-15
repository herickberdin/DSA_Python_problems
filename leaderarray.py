arr = list(map(int,input("Enter the array:").split()))
for i in range(len(arr)):
    flag = True
    for j in range(i+1,len(arr)):
        if arr[j] > arr[i]:
            flag = False
            break
    if flag:
        print(arr[i],end=" ")