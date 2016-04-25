import random, sys, time
from Inventory import Inventory
from Shop import Shop


def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.025)

class Menu:
    
    def Welcome_screen(self):
        print_slow("Basic rules for the game")
        print(".")
        print_slow("your on a mission to sell lemonade")
        print(".")
        time.sleep(2)
        print_slow("and thats it")
        print("..")
        self.main_menu()
        
    def main_menu(self):
        print(".")
        print_slow("MAIN MENU")
        print(".")
        print_slow("what would you like to do?")
        print(".")
        print_slow("Start game")
        print("=1")
        print_slow("view inventory")
        print("=2")
        print_slow("More info")
        print("=3")
        menu_choice=input("")
        buy=Shop()
        if menu_choice== "1":
            buy.purchase_supplies()
        elif menu_choice== "2" :
            self.Inventory_Menu()
        elif menu_choice== "3" :
            self.Info_Menu()
        else:
            print_slow("error")
            return main_menu()
            
    def Inventory_Menu(self):
        print_slow("your inventory consists of")
        Inventory.self.display_inventory
        print("now what?")
        print("1  ")
        print_slow("start game?")
        print("2  ")
        print_slow("or return to main menu")
        choice=input("")
        if choice == "1" :
            self.Store()
        if choice == "2":
            self.main_menu()
    
    def Info_Menu(self):
        print_slow("welcome to more info")
        print("What would you like to know?")
        print("1  ")
        print_slow("more info about the game")
        print("2  ")
        print_slow("rules")
        print("3  ")
        print_slow("you cant handle the info in no 3. just turn around")
        print("4  ")
        print_slow("return to main menu")
        choice=input("")
        if choice == "1":
            print_slow("this game was made on a computer with a keyboared, witn a person and sometimes a mouse was used.")
            return self.Info_Menu()
            
        elif choice == "2":
            print_slow("can you survive in this dog eat dog world? with lemonade stands popping up on every street corner its a booming buisness. Just follow the onboard messages along and make sure not to run out supplies.")
            return self.Info_Menu()
            
        elif choice == "3":
            print_slow("")
            return self.Info_Menu()
            
        elif choice == "4":
            print_slow("lemonade stands are the illuminati")
            return self.Info_Menu()
        else:
            return self.Info.Menu()