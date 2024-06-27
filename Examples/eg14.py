# python program for fibonacci series using simple if..else and for loop

# fibonacci series is the sum of the previous two number to get the succesive terms

a = 0
b = 1
n = int(input("Enter any number: "))
if n < 0:
    print("Fibonacci doesn't exist")
if n == 0:
    print("The fibonacci of 0 is: ",a)
if n == 1:
    print("The fibonacci of 1 is: ",b)
else:
    print(a) #  here we assign the and print values a & b regardless of the conditon as we will need two values to find out the 3rd values in fibonacci
    print(b)
    for i in range(n+1):
        c = a + b   # fibonacci formula is f(n-1) + f(n-2) i.e additon of previous two terms gives the current terms
        a = b
        b = c   # here we swap the values of a, b, c so that we could increment the c value above
        print(c)
#  here we can can use for..else and comment out the a & b print values to just get the value for the specific terms instead of the whole sequence