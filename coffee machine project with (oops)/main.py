

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker=CoffeeMaker()
money_machine=MoneyMachine()
menu=Menu()

should_continue=True

while should_continue:
    option=menu.get_items()
    choice=input(f"What would you like?{option}")
    if choice=="off":
        print("sry the machine is under maintenance")
        should_continue=False
    elif choice=="report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink=menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            money_machine.make_payment(drink.cost)
            coffee_maker.make_coffee(drink)

