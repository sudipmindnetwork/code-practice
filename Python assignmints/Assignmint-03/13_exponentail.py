import math

def calculate_exponential():
    number = float(input("Enter a number to calculate its exponential: "))
    result = math.exp(number)
    print(f"The exponential of {number} is: {result}")

calculate_exponential()
