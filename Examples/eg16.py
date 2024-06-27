#  program for sum of n natural numbers  
num = int(input("Enter number of terms: "))
sum = 0  # we initialize the value of sum so we can add it and store value in it
if num < 0:
    print("Enter positive number")
else:
    #sum = 0
    while num > 0:  #  here we are running the loop till n becomes less than 0
        sum += num
        num -= 1  #  here we decrement the n value to meet the condtion and come out of loop
    print(sum,"is the sum of the given terms")
# here we print the sum out of the loop  as we donot want to print every loop value which will give a sequence of it