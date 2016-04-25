import sys,time,random
from Player import Player
from Menu import Menu
from Shop import Shop
from Inventory import Inventory
from Customers import Customers
from Day import Day
from Lemonade import Lemonade

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.025)
        

onefile=Player()
onefile.Player_Name()
day = Day() 
day.day_Price()
day.getDailyCimate()
day.getTime() 
shop=Shop() 
shop.purchase_supplies() 
day.makeOneCupOfLemonade() 
day.setLemonadePrice() 
