from random import randint
import sys
# Generate number between 1~10
low, high= int(sys.argv[1]), int(sys.argv[2])
print(low)
answer=randint(low,high)
print("answer: ", answer)
# Get input from the user
while True:
    try:
        guess = int(input(f"Guess the number between {sys.argv[1]} and {sys.argv[2]}: "))
        if low < guess < high+1:
            if guess == answer:
                print("Alright, you are a genius")
                break
        else:
            print(f"hey boy I said between {sys.argv[1]} ~ {sys.argv[2]}")
    except ValueError:
        print("Please enter a number")

