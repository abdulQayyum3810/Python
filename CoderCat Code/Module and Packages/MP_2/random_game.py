from random import randint
#Generate number between 1~10
answer=randint(1,10)
print("answer: ", answer)
# Get input from the user
while True:
    try:
        guess = int(input("Guess the number between 1~10:  "))
        if 0 < guess < 11:
            if guess == answer:
                print("Alright, you are a genius")
                break
        else:
            print("hey boy I said 1~10")
    except ValueError:
        print("Please enter a number")

