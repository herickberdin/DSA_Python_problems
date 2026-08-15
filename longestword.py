s=input("Enter a sentence:")
w=s.split()
l=w[0]
for i in w:
    if len(i)>len(l):
        l=i
print(l)