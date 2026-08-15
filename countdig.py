n=int(input("Enter a number:"))
c=0
while(n>0):
    l=n%10
    c+=1
    n//=10
print(c)
    
