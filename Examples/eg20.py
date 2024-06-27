# program to find the hcf/gcd of 2 numbers


def findHCF(x,y):
    if x>y:
        smaller = y   # here we will find the smaller number so that we can iterate a value upto that smaller number
    else:
        smaller = x
    for i in range(1, smaller+1):   # iterating the value upto 'smaller' number to find the hcf
        if((x%i==0)and(y%i==0)):  # here we will check the user input number is divisible by highest iterated number 
            hcf = i    # here we will define a variable to store the highest common factor value
    return hcf    # use return statement to return the defined variable in a function
x = int(input("Enter number: "))
y = int(input("Enter number: "))
print(f"The HCF of {x} and {y} is: ",findHCF(x,y))    #  function calling with user input values