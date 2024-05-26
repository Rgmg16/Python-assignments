# Get user input and split it into a list of strings
numbers_input = input("Enter numbers and separate them with spaces: ").split()

# Convert the list of strings to a list of integers
numbers = list(map(int, numbers_input))

# Iterate through the list with indices using enumerate
for index, value in enumerate(numbers):
    print(f"{value} has an index of {index}")

# Print the list of numbers
print(numbers)

    