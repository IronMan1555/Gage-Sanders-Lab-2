import random
game_number = random.randint(1,10)
print(game_number)
win = False
while(win == False):
    guess = int(input("Pick a random number 1-10: "))
    if guess > game_number:
        print("Too High")
    elif guess < game_number:
        print("Too Low")
    else: 
        print("YOU WIN!")
        win = True