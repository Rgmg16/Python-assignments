def is_prime(number):
    if number <= 1:
        return False
    
    i = 2
    while i * i <= number:
        if number % i == 0:
            return False
        i += 1
    
    return True

number = int(input("Enter a number: "))

if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
