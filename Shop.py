import random, sys, time
from Inventory import Inventory
from Day import Day



def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.025)

class Shop:

    def purchase_supplies(self): 
        supplies=Day() 
        storage=Inventory()
        cash=Inventory()
        supplies.dayPrice() 
        while True: 
            storage.display_inventory() 
            print_slow ("You have: $")
            print(str(cash.Bank)) 
            print_slow("Todays Prices:")
            print (">") 
            print_slow("Lemons: $")
            print(str(round(supplies.priceL, 2)))
            print_slow("Sugar: $")
            print(str(round(supplies.priceS, 2)))
            print_slow("Cups: $")
            print(str(round(supplies.priceC, 2)))
            print_slow("Ice: $")
            print(str(round(supplies.priceI, 2)))
            print("") 
            lemonsPurchased = input("# Lemons you would like to purchase> ") 
            sugarPurchased = input("Ammount of Sugar you would like to purchase> ") 
            cupsPurchased = input("# Cups you would like to purchase> ") 
            icePurchased = input("How much Ice would you like to purchase> ") 
            Total = (float(lemonsPurchased)) * (supplies.priceL) + (float(sugarPurchased)) * (supplies.priceS) + (float(cupsPurchased)) * (supplies.priceC) + (float(icePurchased)) * (supplies.priceI) 
            print_slow("Your total> $")
            print(str(round(Total, 2)))
            print_slow("Are you sure you would like to make this purchase? <enter >: ")
            print("yes or no>")
            confirm = input("")
            if Total > cash.Bank: 
                print_slow("not enough money") 
            elif confirm == "no": 
                print("") 
            else: 
                break           
        cash.Bank-round(Total, 2) 
        list = [Total, lemonsPurchased, sugarPurchased, cupsPurchased, icePurchased] 
        return list 

