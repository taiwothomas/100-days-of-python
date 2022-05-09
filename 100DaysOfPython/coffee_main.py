from coffee_menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from coffee_money_machine import MoneyMachine

menu = Menu()
on = True
coffee_machine = CoffeeMaker()
cash = MoneyMachine()

while on:
    choice = input(f"What would you like? {menu.get_items()}: ")
    if choice != "report" and choice != "off":
        coffee = menu.find_drink(order_name=choice)
        if coffee_machine.is_resource_sufficient(drink=coffee):
            payment = cash.make_payment(cost=coffee.cost)
            if payment:
                serve = coffee_machine.make_coffee(order=coffee)
    elif choice == "report":
        report = {coffee_machine.report(), cash.report()}
    elif choice == "off":
        on = False
