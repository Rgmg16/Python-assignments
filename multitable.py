number = int(input("Enter the number for which you want the multiplication table: "))

num_multiples = int(input("Enter the number of multiples: "))

print(f"Multiplication table for {number} up to {num_multiples} multiples:")
for i in range(1, num_multiples + 1):
    print(f"{number} x {i} = {number * i}")

    