from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
machine_online = True

while machine_online:

    options = menu.get_items()
    order = input(f"What would you like? ({options}): ").lower()

    if order == "off":
        machine_online = False

    elif order == "report":
        coffee_maker.report()
        money_machine.report()

    else:
        drink = menu.find_drink(order)
        if coffee_maker.is_resource_sufficient(drink):
            money_machine.make_payment(drink.cost)
            coffee_maker.make_coffee(drink)

print("Going offline...")




