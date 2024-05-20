def factorial(n):
    
    match n:
        case 0 | 1:
            return 1
        case _ if n < 0:
            raise ValueError("Factorial is not defined for negative numbers.")
        case _:
            return n * factorial(n - 1)

print(factorial(5))  
