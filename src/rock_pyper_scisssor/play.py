"""
This file has all the methods to play with you
"""

import time
import sys
import random
import getch


KEY_MAP = {
    'r': 'Rock!!',
    'p': 'Paper!!',
    's': 'Scissors!!'
}

SLEEP_ENABLED = True



def write_to_screen(text):
    sys.stdout.write(text)


def wipe_screen():
    sys.stdout.write("\x1b[2J\x1b[0;0H")


def read_single_key(question=""):
    if question:
        write_to_screen(question)
    return getch.getch()


def line_seperated_text(text):
    write_to_screen("\n" + text + "\n")


def highlighted_text(text):
    write_to_screen("\n\n" + "="*10 + "\n" + text + "\n" + "="*10 + "\n")


def randomize_outcome():
    return random.choice(["Rock!!", "Paper!!", "Scissors!!"])


def user_won(computer_generated, user_input):

    if computer_generated == user_input:
        return False

    elif computer_generated == "Rock!!" and user_input == "Paper!!":
        return True

    elif computer_generated == "Paper!!" and user_input == "Scissors!!":
        return True

    elif computer_generated == "Scissors!!" and user_input == "Rock!!":
        return True 

    else:
        return False


def sleep_for(time_in_seconds):
    global SLEEP_ENABLED

    if SLEEP_ENABLED:
        time.sleep(time_in_seconds)



def level_1():
    line_seperated_text("Welcome to level 1., Good Luck\n")
    write_to_screen("Pick from Rock-Paper-Scissors, I say Rock, Paper, Scissors... Shoot! and we go!\n\n")

    sleep_for(3)

    sys.stdout.write("\rRock...")
    sys.stdout.flush()
    sleep_for(1)

    sys.stdout.write("\rPaper...")
    sys.stdout.flush()
    sleep_for(1)

    sys.stdout.write("\rScissors...")
    sys.stdout.flush()
    sleep_for(1)

    sys.stdout.write("\rShooooooot!")
    sys.stdout.flush()
    sleep_for(1)

    computer_generated = randomize_outcome()

    highlighted_text(computer_generated)

    return computer_generated


def play_game():
    while True:
        
        computer_generated = level_1()

        player_input = KEY_MAP[str(read_single_key("\n\nWhat was your choice? r / p / s ")).lower()]

        player_won = user_won(computer_generated, player_input)

        if player_won:
            line_seperated_text("\nGood Job. You won !")

        elif player_input == computer_generated:
            line_seperated_text("\nIt's a tie")

        else:
            line_seperated_text("\nAwww! Better luck next time")
        

        play_again = str(read_single_key("\nWould you like to play again? (y/n) \n\n")).lower() == "y"

        if not play_again:
            break

        wipe_screen()
    
    line_seperated_text("\nThanks for playing. Goodbye!\n\n")



if __name__ == "__main__":
    
    play_game()