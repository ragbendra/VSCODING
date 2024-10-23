"""def fib(n):
    if n < 0:
        print("Invalid number.")
    elif n <=1:
        return n
    else:
        return fib(n-1) + fib(n-2)
n = int(input("Enter number of terms: "))
print("The fibonacci series is:")
for i in range(n):
    print(f"The fibonacci number of {i} position is: ",fib(i))"""
    
def fib(n):
    if n < 0:
        print("Invalid number.")
        return
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    
    # Initialize the first two Fibonacci numbers
    a, b = 0, 1
    fibonacci_series = [a, b]  # Store Fibonacci numbers in a list

    # Generate Fibonacci numbers iteratively
    for i in range(2, n):
        a, b = b, a + b  # Update a and b to the next Fibonacci numbers
        fibonacci_series.append(b)  # Add the new Fibonacci number to the list

    return fibonacci_series[:n]  # Return the series up to n terms

n = int(input("Enter number of terms: "))
print("The Fibonacci series is:")
for i, number in enumerate(fib(n)):
    print(f"The Fibonacci number at position {i} is: {number}")