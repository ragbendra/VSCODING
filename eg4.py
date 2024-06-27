def fibonacci(n: int) -> int:
    """Return the nth Fibonacci number"""
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def main() -> None:
    """Get the number of terms from the user and print the Fibonacci series"""
    while True:
        try:
            n = int(input("Enter the number of terms: "))
            if n < 0:
                print("Please enter a positive number.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    print("Fibonacci Series:")
    for i in range(n+1):
        print(fibonacci(i))

if __name__ == "__main__":
    main()