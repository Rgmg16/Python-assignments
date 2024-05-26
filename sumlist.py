list1 = [10,20,30,40,50]
print(f"Sum of numbers in list1:")
sum = 0

for x in list1:
    sum += x
    print(f"Adding {x}, current sum: {sum}")


print(f"Final sum: {sum}")