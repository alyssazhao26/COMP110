"""Ex06 - Choose Your Own Adventure."""
__author__ = "730615172"

from random import randint 

# Collects the player's points.
points: int = 5

# Player Name storage.
player: str = ""

"""Instructions: ends at 7 rounds, win if over 20 pts. 
Choice 1: end game
Choice 2: Route 1: random int being subtract or added ompare to host's value 
Choice 3: Route 2: input int being multiply or added compare to host's value."""

# Emoji Constants
SMILE_EMOJI: str = "\U0001F601"
SAD_FACE_EMOJI: str = "\U0001F61E"
HEART_EMOJI: str = "\U0001F496"
PARTY_EMOJI: str = "\U0001F389"


# Introduction / step 1. 
def greet() -> None:
    """Step 1, introduction."""
    print('Welcome to Number Lotteries')
    global player
    player = f"{input('Who is playing? ')}"
    print(f"Welcome {player}! {SMILE_EMOJI} ")


# Game introduction.
def lottery_1_rule() -> None:
    """Path 1 game rule."""
    print("Rule for number lottery route 1:")
    print("You will have the oppotunity to pick an assignment operator 'Multiply' or 'Plus'.")
    print("Next, you will enter an integer that is less than you current owned points.")
    print("THen, we will combine the points you currently have with the integer you insert for the assignement operator.")
    print("For example, if you have 5 points and you chooce the operator 'multiply' with input integer 3, your number for this round will be 5 * 3 = 15. ")
    print("Meanwhile, the host will also select a random integer from 1 to 20.")
    print("If your number is greater than the host's number, you get 3 points. ")
    print("If your number is smaller, unfortunately we will take 1 points from you.")
    print("If your number equals to my number, you get 10 points! ")


def lottery_2_rule() -> None:
    """Path 2 game rule."""
    print("Rule for number lottery route 2:")
    print("You will have the oppotunity to pick an assignment operator 'Subtract' or 'Plus'.")
    print("Next, we will assign you a random integer between -10 to 10")
    print("Latly, we will combine the points you currently have with the integer you insert for the assignement operator.")
    print("For example, if you have 5 points and you chooce the operator 'subtract' with a random integer -2, your number for this round will be 5 - (-2) = 7. ")
    print("Meanwhile, I will also select a random integer from 1 to 10.")
    print("You will earn 3 points if your number is greater and will lose 1 points if smaller ")
    print("If your number equals to my number, you get 10 points! ")


def num_lot_1() -> None:
    """Number Lottery Path 1."""
    global player
    global points
    print(f"Welcome to lottery path 1, {player}! ")
    lottery_1_rule()
    proceed: str = f"{input('Would you like to proceed to the next step? Please insert 1 for yes or 2 for no: ')}"
    while proceed != '1' and proceed != '2':
        proceed = input('This is not one of the options, please choose again: ')
    if proceed == '2':
        print(f"Thanks for playing, {player} {HEART_EMOJI}! You now have {points} points in this game. See you next time! ")
        return 
    new_int: int = 0
    operator_choice: str = f"{input('Which operator would you like to pick, 1 for multiply and 2 for plus: ') }"
    while int(operator_choice) != 1 and int(operator_choice) != 2:
        operator_choice = input('This is not one of the options, please chooce again: ')
    input_int: int = int(input(f"Please insert an integer that is less than {points}: "))
    while input_int >= points:
        input_int = int(input('The number you inserted is not less than your owned points. Please enter a new integer: '))
    host: int = randint(1, 20)
    if int(operator_choice) == 1:
        new_int = input_int * points
    else:
        new_int = input_int + points
    if new_int < host:
        points -= 1
    elif new_int == host:
        points += 8
    elif new_int > host:
        points += 3
    print(f"Congratulation {player}, you now have {points} points")


def num_lot_2(player_point: int, random_int: int) -> int:
    """Number Lottery Path 2."""
    global player
    print(f'Welcome to lottery path 2, {player}')
    lottery_2_rule()
    proceed: str = f"{input('Would you like to proceed to the next step? Please insert 1 for yes or 2 for no: ')}"
    while proceed != '1' and proceed != '2':
        proceed = input('This is not one of the options, please choose again: ')
    if int(proceed) == 2:
        print(f"See you next time! {HEART_EMOJI} ")
        return player_point
    operator_choice: str = f"{input('Which operator would you like to pick, 1 for subtract and 2 for plus: ') }"
    while int(operator_choice) != 1 and int(operator_choice) != 2:
        operator_choice = input('This is not one of the options, please chooce again: ')
    host: int = randint(1, 10)
    if int(operator_choice) == 1:
        if random_int - player_point < host:
            player_point -= 1
        elif random_int - player_point == host:
            player_point += 8
        elif random_int - player_point > host:
            player_point += 3
    else:
        if random_int + player_point < host:
            player_point -= 1
        elif random_int + player_point == host:
            player_point += 8
        elif random_int + player_point > host:
            player_point += 3
    return player_point


def main() -> None:
    """Entry."""
    global player
    global points
    round_i: int = 1
    total_round: int = 7
    greet()
    print(f"Here is your lottery adventure, {player}! For this game, you will have up to 7 rounds to earn adventure points. You win if you earn 20 points or more.")
    while round_i <= total_round:
        print(f"Round {round_i} / {total_round} ")
        print(f'{player}, you have {points} points now.')
        player_choice: str = input("Please select one of the following options to continue, 1 to enter lottery path 1, 2 to enter lottery path 2, or 3 to exit the game : ")
        while int(player_choice) != 1 and int(player_choice) != 2 and int(player_choice) != 3:
            input('It is not one of the options, please chooce again: ')
        if int(player_choice) == 1:
            num_lot_1()
        elif int(player_choice) == 2:
            random_int: int = randint(-10, 10)
            points = num_lot_2(points, random_int)
            print(f'Congratulations, {player}, you currently have {points} points.')
        elif int(player_choice) == 3:
            print(f"Thanks for playing, {player}! You gained {points} points in this game. See you next time! ")
            return  
        round_i += 1
        if points >= 20:
            print(f"{PARTY_EMOJI} Congratulation, {player}! You have reached 20 points in {round_i} rounds! Thanks for playing!")
            return 
    print(f"{SAD_FACE_EMOJI} Unfortunately {player}, you only have earned {points} points in 5 rounds. Nice try, hope to see you again.")


if __name__ == "__main__":
    main()