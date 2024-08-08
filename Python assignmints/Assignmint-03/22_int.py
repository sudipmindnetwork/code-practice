def calculate_sum_and_average(arr):
    total_sum = sum(arr)
    average = total_sum / len(arr) if arr else 0
    return total_sum, average

numbers = list(map(int, input("Enter a list of integers separated by spaces: ").split()))
total_sum, average = calculate_sum_and_average(numbers)
print(f"Sum: {total_sum}")
print(f"Average: {average}")
