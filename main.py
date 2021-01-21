from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

order = input("What would you like? (espresso/latte/cappuccino): ").lower()

if order == "off":
    machine_online = False

elif order == "report":
    coffee_maker.report()
    money_machine.report()

else:
    menu.find_drink(order)
    print(money_machine.make_payment(0))





