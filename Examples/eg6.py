n = int(input("Enter any numbers: "))
if n < 0:
    print("Enter a positive number")
elif n <= 1:
    print("Not a prime number")
else:
    for i in range(2,n):
        if n % i == 0:
            print(n,"Not a prime number")
            break
    else:
        print(n,"is a Prime number")
        
    