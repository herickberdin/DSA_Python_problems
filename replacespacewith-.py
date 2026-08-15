s=input("Enter the sentence:")
es=""
for i in s:
    if i==" ":
        es+="-"
    else:
        es+=i
print(es)