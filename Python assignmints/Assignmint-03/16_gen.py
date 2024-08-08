def generate_combinations():
    numbers = [1, 2, 3]
    for i in numbers:
        for j in numbers:
            for k in numbers:
                print(f"{i}{j}{k}")

generate_combinations()
