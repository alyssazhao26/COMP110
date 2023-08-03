"""Guess random number and give clues about even or odd, high or low"""
# constant. all captalized letters
SECRET: int = 10

guess: int = int(input('Guess a number! '))
playing: bool = True

while playing:
    if guess == SECRET:
        print("Correct!")
        playing = False
    else: 
        # make sure output and input are the same data type
        if guess % 2 == 1:
            print("Your number is odd, it should be even")
        if guess < SECRET:
            print("it's too low")
        else: # guess is > secret
            print("Too high")
        guess = int(input("Try again "))