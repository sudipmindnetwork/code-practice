def print_8_segment_display():
    n = int(input("Enter the number of lines: "))
    patterns = [
        " _ \n| |\n|_|",
        "   \n  |\n  |",
        " _ \n _|\n|_ ",
        " _ \n _|\n _|",
        "   \n|_|\n  |",
        " _ \n|_ \n _|",
        " _ \n|_ \n|_|",
        " _ \n  |\n  |",
        " _ \n|_|\n|_|",
        " _ \n|_|\n _|"
    ]
    for i in range(n):
        print(patterns[i % 10])

print_8_segment_display()
