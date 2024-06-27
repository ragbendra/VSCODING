# python program for armstrong number in a given range

# armstrongs number is a number which is equal to the sum of the digits raised to the power of the length of the given same number

lower = int(input("Enter lower limit: "))
upper = int(input("Enter upper limit: "))

for num in range(lower, upper+1):
    temp = num   # we store the user num in temporary
    sum = 0  # we initialze this as we will add the total sum in every step
    order = len(str(num))  # we use this as len can't be applied to int type so we convert it to first string then use len to find the num's length
    while temp > 0:   # we want the loop to run till temp is greater than zero
        digit = temp % 10  #  we use % 10 to obtain the  last digit of the given number as dividing the number by 10 gives so
        sum = sum + digit ** (order) #  we raise the power of the digit bye the length of the input digit and add all those in every loop until the loop is stops
        temp //= 10 # we want to eliminate the last digit using floor division so the length of the num keeps decreasing and the loop is satisfied and stops
    if sum == num:  # we will check if sum is equa to num if it is only the it is armstrong else false
        print(num)
