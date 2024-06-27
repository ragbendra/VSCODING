def fibo(n):
    if n<=1:
        return n
    else:
        return fibo(n-1) + fibo(n-2)
n = int(input("Enter any number: "))
if n<0:
    print("Enter positive number")
else:
    for i in range(n+1):
        print(fibo(i))