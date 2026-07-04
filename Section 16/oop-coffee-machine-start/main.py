from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def main():

    # Initialize our objects
    menu = Menu()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()

    # Prompt the user by asking what would you like?
    prompt = input(f"What would you like? ({menu.get_items()})? ")

    while prompt != "off":
        if prompt == "report":
            coffee_maker.report()
            money_machine.report()
        else:
            drink = menu.find_drink(prompt)
            if drink is not None:
                if coffee_maker.is_resource_sufficient(
                    drink
                ) and money_machine.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)
        prompt = input(f"What would you like? ({menu.get_items()})? ")


if __name__ == "__main__":
    main()
