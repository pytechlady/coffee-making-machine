class CoffeeProcess:
    def __init__(self):
        self.ingredient = {
            "water": 300,
            "milk": 200,
            "coffee": 100
        }

    def report(self):
        print(f"Water: {self.ingredient['water']}ml")
        print(f"Milk: {self.ingredient['milk']}ml")
        print(f"Coffee: {self.ingredient['coffee']}g")


    def prepare_coffee(self, order_request):
        for item in order_request.resouces:
            self.ingredient[item] -= order_request.resources[item]
        print(f'Your {order_request} is ready. Enjoy!')