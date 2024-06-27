# python program for prime number using built-in function

#  prime number is a number which is only divisible by 1 and itself where as 
# composite numbr is exactly opposite to it where the number is divisible by other number besides 1 and itself

n = range(2,1000)
def isPrime(n):
    for x in range(2,n): # here we iterate x in the specified range 'n'
        if n % x == 0:  # check the codition for prime number
            return False  # if condition is true will return false
    return True  # else return true
primes = list(filter(isPrime, n)) # filters the values and prints them in a list
print(primes)