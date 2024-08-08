import math
def compute_cosine():
    x = float(input("Enter x: "))
    n = int(input("Enter a positive integer n: "))
    cos_x = 0
    sign = 1
    for i in range(n):
        term = sign * (x**(2*i)) / math.factorial(2*i)
        cos_x += term
        sign *= -1
    return cos_x

print(compute_cosine())
