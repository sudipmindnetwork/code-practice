
n = int(input("Enter a number: "))

a, b = 0, 1

if n >= 0:
    print(a)

while b <= n:
    print(b,end=" ")
    a, b = b, a + b
