def sum_series():
    n = int(input("Enter a positive integer: "))
    total = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            total -= 1 / i
        else:
            total += 1 / i
    return total

print(sum_series())
