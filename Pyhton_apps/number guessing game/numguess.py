import random
EASY_LEVEL_TURNS =10
HARD_LEVEL_TURNS = 5
def check_answer(guess,answer,turns):
    if guess >answer:
        print("Too high. ")
        return turns-1
    elif guess<answer:
        print("Too low.")
        return turns-1
    else:
        print(f"You got it! the answer was {answer}")
    
def set_diffuclty():
    level = input("Choose a diffuclty easy or hard : ")
    if level == "easy":
        turns= EASY_LEVEL_TURNS
    else:
        turns=HARD_LEVEL_TURNS

    return turns
def game():
    answer = random.randint(1,100)
    print("Welcome to number guessing game")
    print("I'm thinking of a number between 1 and 100")



    turns = set_diffuclty()
    
    guess = 0
    while guess != answer:
        print(f"You have {turns} attemts remaining to guess the number")
        guess = int(input("Make a guess : "))

        turns= check_answer(guess, answer,turns)
        if turns ==0:
            print("You run out of gueses you lose ! ")
            return
        elif answer !=guess:
            print("Guess again")

game()