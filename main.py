import random
game_number = random.randint(1,100)
#print(game_number)
win = False
number_of_guesses = 0
while(win == False):
    guess = int(input("Pick a random number 1-100: "))
    number_of_guesses = number_of_guesses + 1
    if guess > game_number:
        print("Too High")
    elif guess < game_number:
        print("Too Low")
    else: 
        print("YOU WIN!")
        win = True
        print("You made it in ", number_of_guesses, " guesses!")
        if number_of_guesses > 10:
            print("You're okay at this game I guess...")
        elif number_of_guesses < 10:
            print("Wow you're actually half decent at this game")