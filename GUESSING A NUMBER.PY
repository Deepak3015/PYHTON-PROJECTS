import random

def guess(x):
    random_variabble = random.randint(1,x)
    guess = 0

    while guess != random_variabble:
        guess = int(input("guess the number"))
        if guess > random_variabble:
            print("guess is high")
        elif guess < random_variabble:5
            print("guess is low ")

    print("wow you guess correct")


guess(10)

