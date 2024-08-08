import math

def solve_quadratic_eqn(a, b, c):
    if a == 0:
        raise ValueError("Coefficient 'a' cannot be zero for a quadratic equation.")
    
    discriminant = b**2 - 4*a*c
    
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return (root1, root2)
    elif discriminant == 0:
        root = -b / (2*a)
        return (root,)
    else:
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(-discriminant) / (2*a)
        return (complex(real_part, imaginary_part), complex(real_part, -imaginary_part))

# Example usage:
a = 1
b = -3
c = 2
solutions = solve_quadratic_eqn(a, b, c)
print("The solutions of the quadratic equation are:", solutions)
