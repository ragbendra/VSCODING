"""n = int(input("Enter number of terms: "))
if n < 0:
    print("Enter positive number.")
elif n<=1:
    print("Not a prime number.")
elif n==2:
    print("Prime Number")
else:
    for i in range(3,n+1):
        if n%i == 0:
            print(n,"is not a prime number")
            break
    else:
        print(n,"is a prime number")"""
        


import math

n = int(input("Enter a number: "))

# Handle edge cases for numbers less than or equal to 1
if n <= 1:
    print(f"{n} is not a prime number.")
    
# 2 is the only even prime number
elif n == 2:
    print(f"{n} is a prime number.")

# For numbers greater than 2
else:
    is_prime = True
    # Check divisibility from 2 up to the square root of n
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:  # If n is divisible by any number in this range
            is_prime = False
            break
    
    if is_prime:
        print(f"{n} is a prime number.")
    else:
        print(f"{n} is not a prime number.")