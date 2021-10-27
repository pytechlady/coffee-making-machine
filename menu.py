class Menu:
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        self.resources = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }
class MenuList:
    def __init__(self):
        self.avail_menu = [
            Menu(name="espresso", water=50, coffee=18, milk=5, cost=1.5),
            Menu(name="latte", water=200, coffee=24, milk=150, cost=2.5),
            Menu(name="cappuccino", water=250, coffee=24, milk=100, cost=3.0),
        ]
    def fetch_item(self):
        choice = ""
        for i in self.avail_menu:
            choice += f"{i.name}/"
        return choice

    def search_drink(self, drink_name):
        for item in self.avail_menu:
            if item.name == drink_name:
                return item
        print("Sorry that drink is not available")