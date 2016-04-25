import random, sys, time
from Lemonade import Lemonade


def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.025)


 
class Day:

    priceL=0
    pricec=0
    priceS=0
    priceI=0
    temp=None
    weather=None

    def __init__(self): 
        self.priceL
        self.priceC
        self.priceS
        self.priceI
        self.temp
        self.weather
        
    def day_Price(self): 
        for item in range (1,2): 
            self.priceL = random.uniform (.5,.9) 
        for item in range (1,2): 
            self.priceC = random.uniform (1,3) 
        for item in range (1,2): 
            self.priceS = random.uniform(5,10) 
        for item in range (1,2): 
            self.priceI = random.uniform(.01, .03) 
            

        
    def makeOneCupOfLemonade(self): 
        print_slow("1. Keep or 2. change recipe?")
        print(">")
        AskToChangeRecipe = input("") 
        if (AskToChangeRecipe.lower() == "yes"): 
            self.lemonsinCup = input("How many lemons do you want to add? >") 
            self.lemonsinCup = int(self.lemonsinCup) 
            self.sugarinCup = input("How many cups of sugar? >") 
            self.sugarinCup = int(self.sugarinCup) 
            self.icePerCup = input("How much ice do you want to add? >") 
            self.icePerCup = int(self.icePerCup) 
            self.lemonade = Lemonade(self.lemonsinCup,self.sugarinCup,self.iceinCup) 
        else: 
            self.lemonade.setRecipe(self.lemonade.lemonsinCup, self.lemonade.sugainrCup, self.lemonade.iceinCup) 

    def setLemonadePrice(self): 
        while True: 
            price=input("enter the price of a cup of lemonade between 1 and 100>  ")
            price=round(float(price),2) 
            if 0 <= price <= 101: 
                print_slow("The price of lemonade has been set to>")
                print(price)
                break 
            else:
                print("Invaild Entry 1 - 100") 

            
    def sellLemonade(self): 
        if self.supply.lemons >= self.lemonsPerCup and self.supply.sugar >= self.sugarPerCup and self.supply.cups > 0: 
            self.supply.lemons -= self.lemonsPerCup 
            self.supply.sugar -= self.sugarPerCup 
            self.supply.cups -= 1 
        elif self.supply.lemons<self.lemonsPerCup: 
            print ("Not enough lemons" )
        elif self.supply.sugar<self.sugarPerCup: 
            print ("Not enough sugar" )
        elif self.supply.cups<=0: 
            print ("No cups left" )
        else: 
            print ("Can't sell lemonade, not enough supplies" )


  
    def Run(self):
        for x in range(1,1000):
            x=Customers.get_customer
            if x%2 == 0:
                Customers.customer1
            elif x%3 == 0:
                Customers.customer2
            else:
                print("noones around")
            End_day()
        
    def End_day(self):
        print("0")
        print_slow("you made a total of >")
        print(display_register)
        print_slow("moving money to bank......")
        time.wait(2)
        Menu.Welcome_screen
        
