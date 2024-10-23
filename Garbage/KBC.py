questions = [["What is the your name?","Shubham","Saiju","prajwal","Kushal","none",3],
             ["What is the your age?","20","21","22","23","none",4],
             ["What is the your gender?","male","female","other","Trans","none",3],
             ["What is the your city?","Bangalore","Mumbai","Hyderabad","Chennai","none",4],
             ["What is your branch?","CSE","ECE","EEE","Civil","none",1],
             ["How are you?","Good","Fine","Bad","Shit","none",3],
             ["What is your aim?","Eng","Sci","Doc","Nothing","none",4],
             ["What is your hobby?","Cricket","Football","Reading","none",3],
             ["What are you?","Human","Animal","God","Demon","none",1]]

levels=[1000,5000,7000,10000,20000,30000,50000,100000,320000]

money = 0
for i in range(0,len(questions)):
    question = questions[i]
    print(f"Questions for Rs.{levels[i]} is:")
    print(f"a. {question[1]}              b. {question[2]}")
    print(f"c. {question[3]}              d. {question[4]}")
    reply = int(input("Enter the option (1-4): "))
    if reply == question[-1]:
        print(f"Congrats you have won Rs.{levels[i]}")
        if i == 1:
            money = 1000
        elif i == 4:
            money = 10000
        elif i == 8:
            money = 50000 
    else:
        print("You have lost.")
        break
print(f"The total amount you have won is Rs.{money}")