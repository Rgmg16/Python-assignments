def multiply_numbers(*args):
     
    product = 1
    for num in args:
        product *= num
    return product

print(multiply_numbers(1, 2, 3, 4, 5))

