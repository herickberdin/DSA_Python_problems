n=int(input("Enter the number:"))
arr=list(map(int,input("Enter the array:").split()))
freq={}
for i in arr:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
for j in freq:
    if freq[j]>1:
        print("The duplicate elements are:",j)