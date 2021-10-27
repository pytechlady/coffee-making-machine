class Payment:
    coin_values = {
        "Pennies": 0.01, "Nickles": 0.05, "Dimes": 0.10, "Quarters": 0.25}

    currency_accepted = "$"

    def __init__(self):
        self.amount_made = 0
        self.amount_paid = 0

    def report(self):
        print(f'Balance: {self.currency_accepted}{self.amount_made}')

    def confirm_coin(self):
        print("Please insert coins")
        for item in self.coin_values:
            self.amount_paid += int(input(f'How many {item}?: ')) * float(self.coin_values[item])
        print(f'Total: {self.amount_paid}')
        return self.amount_paid


    def make_payment(self, cost):
        self.confirm_coin()
        if self.amount_paid >= cost:
            customer_balance = round(self.amount_paid - cost, 2)
            self.amount_made += cost
            print(f'Kindly take your coffee. Here is your balance {self.currency_accepted}{customer_balance}')
            return customer_balance
        else:
            print(f'Insufficient coins. {self.currency_accepted}{self.amount_paid} payment refunded')
        self.amount_paid = 0