#proram to print the binary of any number using recursive function

"""def convertBinary(n):
    if n>1:
        convertBinary(n//2)
    print(n%2,end="")
convertBinary(15)"""

def convertBinary(n):
    return bin(n).replace("0b"," ")  # here we used bin function to return the binary of the decimal or other input and 
#  use replace function to replace the '0b' with an empty space 
# because when we print the bin of any number python prints the binary nof that number with 0b prefix to show its the binary number
print(convertBinary(15))

n=int(input("Enter: "))
print(bin(n))  # will print the 0b1111