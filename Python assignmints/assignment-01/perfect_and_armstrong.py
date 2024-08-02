
def is_perfect_number(num):
    if num <= 0:
        return False
    sum_of_divisors = 0
    for i in range(1, num):
        if num % i == 0:
            sum_of_divisors += i
    return sum_of_divisors == num

def is_armstrong_number(num):
    if num <= 0:
        return False
    order = len(str(num))
    sum_of_digits = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum_of_digits += digit ** order
        temp //= 10
    return sum_of_digits == num

num = int(input("Enter a number: "))

if is_perfect_number(num):
    print(f"{num} is a perfect number.")
else:
    print(f"{num} is not a perfect number.")

if is_armstrong_number(num):
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
