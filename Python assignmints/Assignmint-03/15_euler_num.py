import math

def compute_euler(n):
    euler = sum(1 / math.factorial(i) for i in range(n + 1))
    return euler

n = int(input("Enter the number of terms to compute Euler's number: "))
print(f"The value of Euler's number is: {compute_euler(n)}")
