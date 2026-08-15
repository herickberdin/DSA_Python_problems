n=int(input("Enter the number:"))
arr=list(map(int,input("Enter the array:").split()))
freq={}
for i in arr:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
for j in freq:
    print(j,"-",freq[j])