arr=list(map(int,input("Enter the array:").split()))
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]==arr[j]:
            print("The first repeating element is:",arr[i])
            break
    else:
        continue
    break
else:
    print("No repeating element")