s=[]
brackets=input("Enter the brackets:")
flag=True
pairs={')':'(',']':'[','}':'{'}
for i in brackets:
    if i in '({[':
        s.append(i)
    elif i in '}])':
        if len(s)==0:
            flag=False
            break
        if s[-1]==pairs[i]:
            s.pop()
        else:
            flag=False
            break
if len(s)!=0:
    flag=False
if flag:
    print("Balanced")
else:
    print("not balanced")