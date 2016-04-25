import random, sys, time
from Menu import Menu


def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.025)

class Player:
                
    def Player_Name(self):
    
        print_slow("Time to play LEMONADE STAND")
        print(".")
        print_slow("Whats your name?>")
        name=input("")
        Player=name
        print_slow("Welcome,")
        print(Player)
        print_slow(" to the most intense way to spend a nice sunny day!!")
        print(".")
        print_slow("Are you ready to play?>")
        answer=input("")
        menu=Menu()
        if answer=="yes":
            menu.Welcome_screen()
        else:
            print_slow("are you sure you want to quit?")
            answer_two=input("")
            if answer_two=="no":
                menu.Welcome_screen()
            else:
                print_slow("too bad :)")
                menu.Welcome_screen()