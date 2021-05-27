class CoffeeStack:
    """
    Class containing supplies in Coffee machine
    and recipes for Espresso, Cappuccino, Latte, Ice coffee
    + extras - milk, sugar, flavor
    """

    def __init__(self):
        self.coffee_beans = 10
        self.milk = 10
        self.ice_cubes = 10
        self.sugar = 5
        self.flavor = 5

    def espresso(self):
        self.coffee_beans -= 2

    def cappuccino(self):
        self.coffee_beans -= 2
        self.milk -= 2

    def latte(self):
        self.coffee_beans -= 2
        self.milk -= 4

    def ice_coffee(self):
        self.coffee_beans -= 2
        self.ice_cubes -= 4

    def add_extra_shot(self, amount=1):
        self.coffee_beans -= amount

    def add_sugar(self, amount=1):
        self.sugar -= amount

    def add_vanilla_flavor(self, amount=1):
        self.flavor -= amount


class CoffeeMachine(CoffeeStack):
    """
    Class simulating coffee machine. It can prepare coffees,
    you can add extra shot, sugar or vanilla flavor
    If you run out of stock, machine needs refill. You can check current stock status
    """

    def stock_checker(self):
        "Checking if enough stock in machine for making drink"
        stock = {
            "coffee beans": self.coffee_beans,
            "milk": self.milk,
            "ice": self.ice_cubes,
            "sugar": self.sugar,
            "flavor": self.flavor
        }
        for item in stock.values():
            if item < 0:
                return False
            return True

    def make_coffee(self, coffee_type):
        "Making coffee if enough stock in machine. If not, it gives alert for refill"
        coffe_types = ["espresso", "cappuccino", "latte", "ice_coffee"]
        if coffee_type in coffe_types:
            eval("self." + coffee_type + "()")
            if self.stock_checker():
                print(f"Here is your {coffee_type}! Enjoy your drink!")
            else:
                print("Sorry we are out of stock! Machine needs to be refilled")
        else:
            return "Sorry we don`t have this drink"

    def extras(self):
        "Asking if customer wnats to add extras"
        extras = input("type if you want to add extra 'coffee shot', 'sugar', 'vanilla flavor' or 'no' ")
        if extras == "coffee shot":
            self.add_extra_shot()
            return "Extra shot added"
        if extras == "sugar":
            self.add_sugar()
            return "Sugar added"
        if extras == "vanilla flavor":
            self.add_vanilla_flavor()
            return "Flavor added"
        if extras == "no":
            return "No extras"
        else:
            return "Wrong input! No extras added!"

    def show_stock(self):
        "Showing how much stock is in coffee machine"
        stock = {
            "coffee beans": self.coffee_beans,
            "milk": self.milk,
            "ice": self.ice_cubes,
            "sugar": self.sugar,
            "flavor": self.flavor
        }
        return stock

    def refill_machine(self):
        "Set values to default setup"
        self.coffee_beans = 10
        self.milk = 10
        self.ice_cubes = 10
        self.sugar = 5
        self.flavor = 5
        return "Machine refilled!"


def terminal():
    """Interface for Coffee Machine"""
    print("Hello Coffee Lover!")
    start = True
    coffee_machine = CoffeeMachine()
    while start:
        print("""
        Please choose your drink: 
        1: 'espresso'
        2: 'cappuccino'
        3: 'latte'
        4: 'ice coffee'
        5: 'maintanance'
        q: 'quit'
        """)
        choice = input("Choose your drink by name or number:")
        if choice in ["1", "espresso"]:
            coffee_machine.extras()
            coffee_machine.make_coffee("espresso")
            continue

        if choice in ["2", "cappuccino"]:
            coffee_machine.extras()
            coffee_machine.make_coffee("cappuccino")
            continue

        if choice in ["3", "latte"]:
            coffee_machine.extras()
            coffee_machine.make_coffee("latte")
            continue

        if choice in ["4", "ice coffee"]:
            coffee_machine.extras()
            coffee_machine.make_coffee("ice_coffee")
            continue

        if choice in ["5", "maintanance"]:
            technican_action = input("Choose from options: '1: show stock' '2: refill machine'")
            if technican_action in ["1", "show stock"]:
                print(coffee_machine.show_stock())
                continue
            if technican_action in ["2", "refill machine"]:
                print(coffee_machine.refill_machine())

        if choice in ["q", "quit"]:
            print("Bye Bye")
            return

        else:
            print("Invalid input! Please try again or type 'q', 'quit' for exit")
            continue


if __name__ == "__main__":
    terminal()
