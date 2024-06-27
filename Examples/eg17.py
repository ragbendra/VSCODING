#  program to display the power of 2 using anonymous function 

"""nterms = int(input("Enter number of terms here: "))
#  we  use anonymous function and use map function it will put all the function in an iterable and use list to print it in list  
result = list(map(lambda x : 2 ** x, range(nterms+1)))
print(result)

for i in range(nterms+1):
    print(f"the value of 2 raised to power {i} is",result[i])
#  we can also use list comprehension
result = [2 ** i for i in range(nterms+1)]
print(result)
#  we can also use for loop
result = []
for i in range(nterms+1):
    result.append(2 ** i)
    print(result)"""
#  we can also use generator expression
nterms = int(input("Enter any number: "))
result = (2 ** i for i in range(nterms+1))
for i in result:
    print(i)
"""#  we can also use recursion
def power(n):
    if n == 0:
        return 1
    else :
        return 2 * power(n-1)
result = [power(i) for i in range(nterms+1)]
print(result)
    """

