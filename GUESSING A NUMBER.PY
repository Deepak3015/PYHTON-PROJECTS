import random

# def guess(x):
#     random_variabble = random.randint(1,x)
#     guess = 0

#     while guess != random_variabble:
#         guess = int(input("guess the number"))
#         if guess > random_variabble:
#             print("guess is high")
#         elif guess < random_variabble:5
#             print("guess is low ")

#     print("wow you guess correct")


# guess(10)

import random

def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f"Is {guess} too high (h), too low (l), or correct (c)? ").lower()

        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1

    print(f"Yes, you were correct! The computer guessed your number: {guess}.")




computer_guess(10)



          

            
