#Simple Quiz Joseph Rydberg 9/30/2024
from random import randrange


def choose_quiz():
    x = randrange(1, 50)
    y = randrange(1, 100)
    print("What is", x, "+", y)

    answer = x + y
    return answer

def take_quiz():
    answer = choose_quiz()
    guess = float(input())

    if guess == answer:
        print("Correct")
    else:
        print("Incorrect")

take_quiz()