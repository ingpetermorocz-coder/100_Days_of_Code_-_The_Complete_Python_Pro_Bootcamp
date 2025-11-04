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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def report():
    print(f"Water: {current_resources["water"]}ml")
    print(f"Milk: {current_resources["milk"]}ml")
    print(f"Coffee: {current_resources["coffee"]}g")
    print(f"Money: ${cashier}")

def check_resources(drink,res):
    is_enough_res = True
    if res["water"] < MENU[drink]["ingredients"]["water"]:
        print("Sorry, there is not enough water.")
        is_enough_res = False
    if res["coffee"] < MENU[drink]["ingredients"]["coffee"]:
        print("Sorry, there is not enough coffee.")
        is_enough_res = False
    if drink == "latte" or drink == "cappuccino":
        if res["milk"] < MENU[drink]["ingredients"]["milk"]:
            print("Sorry, there is not enough milk.")
            is_enough_res = False
    return is_enough_res

def process_coins():
    print("Please insert coins.")
    q = int(input("how many quarters?: "))
    d = int(input("how many dimes?: "))
    n = int(input("how many nickles?: "))
    p = int(input("how many pennies?: "))
    inserted = float(0.25 * q + 0.10 * d + 0.05 * n + 0.01 * p)
    return inserted

def check_transaction(drink,total):
    is_enough_coin = True
    if MENU[drink]["cost"] > total:
        print("Sorry that's not enough money. Money refunded.")
        is_enough_coin = False
    return is_enough_coin

def make_coffee(drink,res):
    water = res["water"] - MENU[drink]["ingredients"]["water"]
    coffee = res["coffee"] - MENU[drink]["ingredients"]["coffee"]
    if drink == "latte" or drink == "cappuccino":
        milk = res["milk"] - MENU[drink]["ingredients"]["milk"]
    else:
        milk = res["milk"]
    return water, milk, coffee

machine_on = True
current_resources = resources
cashier = 0
while machine_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "espresso" or choice == "latte" or choice == "cappuccino":
        enough_resources = check_resources(drink=choice,res=current_resources)
        if enough_resources:
            total_coins = process_coins()
            check_transaction(drink=choice,total=total_coins)
            if check_transaction:
                change = total_coins - MENU[choice]["cost"]
                print(f"Here is ${round(change,2)} in change.")
                new_resources = make_coffee(drink=choice,res=current_resources)
                current_resources = {"water": new_resources[0], "milk": new_resources[1], "coffee": new_resources[2]}
                cashier += round(total_coins - change, 2)
                print(f"Here is your {choice} \U00002615. Enjoy!")
    elif choice == "off":
        machine_on = False
    elif choice == "report":
        report()
    else:
        print("Wrong input!")
