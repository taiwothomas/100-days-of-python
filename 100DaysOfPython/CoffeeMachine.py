MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def cost(coffee):
    money = MENU[coffee]['cost']
    return money


def ing(coffee):
    stuff = MENU[coffee]['ingredients']
    return stuff


stock = {}
cash = 0
finished = ""
stock_logic = True

while True:
    choice = input("What would you like? espresso/latte/cappuccino: ")

    if choice != 'report' and choice != 'off' and stock_logic:
        price = cost(choice)
        print("Please insert coins.")
        quarters = float(input("How many quarters? ")) * .25
        dimes = float(input("How many dimes? ")) * .1
        nickels = float(input("How many nickels? ")) * .05
        pennies = float(input("How many pennies? ")) * .01
        total = quarters + dimes + nickels + pennies

        if total > price:
            cash += total
            for thing in ing(choice):
                stock[thing] = resources[thing] - ing(choice)[thing]
            change = round(cash - price, 3)
            cash -= change
            stock['cash'] = cash
            print(f"Your change is ${change}. Enjoy your {choice} ☕")
            stock_logic = stock['water'] > ing(choice)['water'] and stock['milk'] > ing(choice)['milk'] and stock[
                'coffee'] > ing(choice)['coffee']
        elif price > total:
            print("Sorry that's not enough money. Money refunded")
        else:
            print(f"No change. Enjoy your {choice} ☕")

    elif choice != 'report' and choice != 'off' and not stock_logic:
        for thing in stock:
            if thing != 'cash':
                if stock[thing] < ing(choice)[thing]:
                    finished = thing
        print(f"Sorry there is not enough {finished} for {choice}")
    elif choice == 'report':
        print(f"Water: {stock['water']}ml\nMilk: {stock['milk']}ml\nCoffee: {stock['coffee']}mg\n"
              f"Cash: ${stock['cash']}")

    elif choice == 'off':
        exit()
