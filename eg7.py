import random
secret_number = random.randint(1,100)
guess = int(input("Enter anymber less than 100: "))
if guess == secret_number:
    print("You win")
else:
    print("You lose")