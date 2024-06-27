# program to find a number divisible by another number using lambda function

# here we will take user input list values and use it in lamda function
#  we can do so by 2 methods written below

# method 1
# input() to read input + split() to split the input on spaces 
# + [f(x) for x in iter] to loop over each of those + int to turn each into an int

l = [int(x) for x in input().split()] 
result = list((lambda x : x % 16 == 0, l))
print(result)


l = [int(x) for x in input().split()] 
num = int(input("Enter any number: "))
result = list((lambda x, num : x % num == 0, l))
print(result)

# method 2
"""s = input()
l = list(map(int, s.split()))
result = list(filter(lambda x : x % 16 == 0, l))
print(result)"""
