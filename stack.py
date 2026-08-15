s=[]
print("1.push")
print("2.pop")
print("3.peek")
print("4.display")
print("5.exit")
while True:
    ch=int(input("Enter your choice:"))
    if ch==1:
        n=int(input("Enter a number:"))
        s.append(n)
    elif ch==2:
        if len(s)==0:
            print("Empty stack")
        else:
            s.pop()
    elif ch==3:
        if len(s)==0:
            print("Empty")
        else:
            print("The last element is:",s[-1])
    elif ch==4:
        for i in range(len(s)-1,-1,-1):
            print(s[i])
    elif ch==5:
        print("over")
        break