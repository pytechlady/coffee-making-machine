# Entry point of the application
from menu import MenuList
from coffee_process import CoffeeProcess
from payment import Payment

def start_machine():
    print("WELCOME TO BIM'S COFFEE SHOP")

menu = MenuList()
coffee_process = CoffeeProcess()
payment = Payment()
start_machine()
is_on = True
while is_on:
    choice = menu.fetch_item()
    request_prompt = input(f"What would you like to have? {choice}: ").lower()
    if request_prompt == "off":
        print("GOODBYE")
        is_on = False
    elif request_prompt == "report":
        coffee_process.report()
        payment.report()
    elif request_prompt == "latte" or request_prompt == "espresso" or request_prompt == "cappuccino":
        drink = menu.search_drink(request_prompt)
        sufficient_money = payment.make_payment(drink.cost)
    else:
        print("Your request cannot be processed")





start_machine()
