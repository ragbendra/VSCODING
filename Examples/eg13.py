# python program for factorial of a given number using recursion

#  factorial is the multiplication of a number to its one lesser number i.e n * (n-1)

def isFact(n):
    if n<0:  # check the conditon and print the result
        print("Enter positive number")
    elif n==0:   # check and return 1
        return 1
    else :
        return n * isFact(n-1)  # (recursive function as it calls itself i.e calls 'n')actual conditon for factorial 
                                #  here we multiply the number n with its factorial ie. factorial of n-1 and multiply the n-1 with its factorial which will be (n-1)-1 and so on 
n = int(input("Enter any number: "))

print(isFact(n))


# method 2 using if else and for loop

num = int(input("Enter any number: "))
fact = 1
if num < 0 :
    print("Factorial doesn't exist")
if num == 0:
    print("Factorial of 0 is", 1)
else:
    for i in range(1, num + 1):
        fact *= i      # here we check the conditon and print it 
print("The factorial of the givern number is: ", num)   # the print function is outside the for loop because we dont want to print all the values iterated in the loop

    