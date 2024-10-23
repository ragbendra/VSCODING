# de"""f name(a: int, b: str):
#     print(a)
#     print(b)
#     print(type(a))
#     print(type(b)) 
# name("ee",8)

"""def multiply_numbers(a: float, b: float) -> float:
    # Type casting arguments to floats
    a = float(a)
    b = float(b)
    return a * b

# Calling the function with integers
result = multiply_numbers(3, 4)
print(result)  # Output will be 12.0

"""
# n=eval(input("Enter the valuve of n : "))
# sum=0
# for i in range (n+1):
#     if i%2==0:
#         sum+=i
# print(sum)

n=input("Enter anything: ")
print(len(n))
rev=""
for i in n:
    rev=i+rev
if n==rev:
    print(n,"is palindrome")
else:
    print(n,'is not palindrome')
count=0
for count,i in enumerate(n):
    # count+=1
    print(count,i)