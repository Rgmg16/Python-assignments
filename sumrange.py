number= int(input("Enter a number here: "))
lastnum= int(input("Enter a final number here: "))

print(f"Sum of numbers from {number} to {lastnum}:")
sum = 0

for x in range(number, lastnum + 1):
    sum += x
    print(f"Adding {x}, current sum: {sum}")


print(f"Final sum: {sum}")