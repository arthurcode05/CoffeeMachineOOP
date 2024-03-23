from coffee_maker import CoffeeMaker
from menu import MenuItem, Menu
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True
while is_on:
    choice = input("What would you like? latte/cappuccino/espresso ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(coffee_maker.report())
    else:
        drink = menu.find_drink(choice)
        money_machine.make_payment(drink.cost)
        if coffee_maker.is_resource_sufficient(drink):
            coffee_maker.make_coffee(drink)
