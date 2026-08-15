rev=0
n=int(input("Enter a number to reverse:"))
while(n>0):
    l=n%10
    rev=rev*10+l
    n//=10
print(rev)
