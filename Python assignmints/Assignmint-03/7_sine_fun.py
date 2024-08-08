import math

def compute_sine():
    x = float(input("Enter x: "))
    n = int(input("Enter a positive integer n: "))
    sine_x = 0
    sign = 1
    for i in range(n):
        term = sign * (x**(2*i+1)) / math.factorial(2*i+1)
        sine_x += term
        sign *= -1
    return sine_x

print(compute_sine())
