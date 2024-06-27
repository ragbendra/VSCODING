# python program to calculate the timetaken to extecute the program
import time
def myFunc():
    start_time = time.time()
    s = 0
    for i in range(1, n+1):
        s = s + i
    end_time = time.time()
    return s, end_time - start_time
n = int(input("Enter a number: "))
print(myFunc())