n=int(input("Enter a number:"))
sum=0
while(n):
    l=n%10
    sum+=l
    n=n//10
print(sum)
