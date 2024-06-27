# python program for armstrong number
num = int(input("Enter any number: "))
sum = 0
temp = num
if num < 0:
    print("Enter positive number")
else:
    while(temp>0):
        digit = temp % 10
        sum = sum + digit**3
        temp = temp // 10
    if sum == num:
        print("Armstrong number")
    
    else:
        print("Not an Armstrong number")