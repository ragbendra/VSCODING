# python program for prime number between a range

lower = int(input("Enter lower limit: "))
upper = int(input("Enter upper limit: "))
print("Prime numbers between", lower, "and", upper, "are:")
for num in range(lower, upper+1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                print(num,"is not a prime number")
                break
        else:
            print(num,"is a prime number")
                