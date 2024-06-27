n = int(input("Enter any number: "))
sum = 0
for i in range(2,n+1):
    if n % i == 0:
        print("Not a Prime number")
    else:  
        print(n,"is prime number")
