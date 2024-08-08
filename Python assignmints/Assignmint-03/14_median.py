def find_median(numbers):
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_numbers[mid - 1] + sorted_numbers[mid]) / 2
    else:
        return sorted_numbers[mid]

numbers = list(map(int, input("Enter a set of numbers separated by spaces: ").split()))
print(f"The median is: {find_median(numbers)}")
