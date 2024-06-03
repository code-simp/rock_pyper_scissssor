"""
This file has all the methods to play with you
"""

import time
import sys
import random
import getch
import string


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


def level_1():
    line_seperated_text("Welcome to level 1., Good Luck")
    write_to_screen("Pick from Rock-Paper-Scissors, I say Rock, Paper, Scissors... Shoot! and we go!\n\n")

    time.sleep(3)

    sys.stdout.write("\rRock...")
    sys.stdout.flush()
    time.sleep(1)

    sys.stdout.write("\rPaper...")
    sys.stdout.flush()
    time.sleep(1)

    sys.stdout.write("\rScissors...")
    sys.stdout.flush()
    time.sleep(1)

    sys.stdout.write("\rShooooooot!")
    sys.stdout.flush()
    time.sleep(1)

    highlighted_text(randomize_outcome())


def play_game():
    while True:
        
        level_1()

        player_won = str(read_single_key("\n\nDid you win? (y/n) ")).lower() == "y"

        if player_won:
            line_seperated_text("Good Job. You won !")

        else:
            line_seperated_text("\nAwww! Better luck next time")
        

        play_again = str(read_single_key("\n\nWould you like to play again? (y/n) \n\n")).lower() == "y"

        if not play_again:
            break

        wipe_screen()
    
    line_seperated_text("\nThanks for playing. Goodbye!\n\n")



if __name__ == "__main__":
    
    play_game()