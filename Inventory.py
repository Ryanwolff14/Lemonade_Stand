import random, sys, time

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.025)

class Inventory:

    Bank=100.00
    lemons=0
    sugar=0
    cups=0
    ice=0
    lemonade=0

    def _init_(self):
        self.lemons
        self.sugar
        self.cups
        self.lemonade
        
    def addToSupplies(self,listOfItemsPurchased): 
        self.lemons += listOfItemsPurchased[1] 
        self.sugar += listOfItemsPurchased[2] 
        self.cups += listOfItemsPurchased[3] 
        self.ice += listOfItemsPurchased[4] 
        
    def display_inventory(self): 
        print_slow("You Have  ") 
        print ("Lemons " , str(self.lemons))
        print ("Sugar " , str(self.sugar))
        print ("Cups " , str(self.cups))
        print ("Ice " , str(self.ice))

        
