def calculate_slope(x1, y1, x2, y2):
    if x1 == x2:
        raise ValueError("Slope is undefined for vertical lines (x1 cannot be equal to x2).")
    return (y2 - y1) / (x2 - x1)

x1=int(input("Enter x1 : "))
x2=int(input("Enter x2 : "))
y1=int(input("Enter y1 : "))
y2=int(input("Enter y2 : "))
slope = calculate_slope(x1, y1, x2, y2)
print("The slope of the line is:", slope)
