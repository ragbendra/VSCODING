x=10
print(x)
def hello():
    #global x
    x=5
    y=7
    print(f"The local value is {x}")
    print("Hello")
print(f"The global value is {x}")
x=4
hello()
#print(f"The global value is {y}")
print(f"The global value is {x}")
