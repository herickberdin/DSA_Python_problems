n = int(input("How many numbers? "))

a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    next = a + b
    a = b
    b = next
