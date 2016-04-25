import random, sys, time

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.025)

class Customers:

    def buyLemonade(self): 
        chanceOfBuying = None 
        day=Day() 
        day.getDailyClimate() 
        day.setLemonadePrice() 
        if day.weather == "sunny" and day.temp > 80 and day.price < 70: 
            chanceOfBuying = 0.95 
        elif day.weather == "rainy" and day.temp < 60 and day.price > 90: 
            chanceOfBuying = 0.80 
        elif day.weather == "humid" and 60 <= day.temp <= 80 and 70 <= day.price <= 90: 
            chanceOfBuying = 0.85 
        elif day.price == 69: 
            chanceOfBuying = 1  
        else: 
            chanceOfBuying = 0.75 
        if random.random() <= chanceOfBuying: 
            day.sellLemonade() 