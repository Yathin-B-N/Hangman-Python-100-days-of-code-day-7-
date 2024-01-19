# TODO: 2. Check for all coffee machine resources sufficiency


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

profit = 0
def is_resource(order_ing):
    for item in order_ing:
        if resources[item]<=order_ing[item]:
            print(f"Sorry we dont have enough {item}")
            return False
    return True
def insert_coins():
    """return the total calculated from coins"""
    print("Please insert coins")
    coins = {"quaters":0.25, "dimes":0.10, "nickles":.05, "pennies":.01}
    total=0
    for i in coins:
        total += float(input(f"How many {i}?:"))*coins[i]
    return total

def make_coffee(drink_name,order_ing):
    """deduct the ingredients from the resources"""
    for item in order_ing:
        resources[item]=resources[item]-order_ing[item]
    print(f"here is your drink {drink_name}")

def is_trans_successful(money_recived,drink_cost):
    if money_recived>=drink_cost:
        change = round(money_recived-drink_cost,2)
        print(f"here is ${change} in change ")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money.Money refunded")
        return False
# TODO: 1. Print report of all coffee machine resources
is_on = True

while is_on:
    ip = input('What would you like? (espresso/latte/cappuccino:)').lower()
    if ip == "off":
        is_on = False

    elif ip == "report":
        print(f"water:{resources['water']}ml\nmilk:{resources['milk']}ml\ncoffee:{resources['coffee']}g\n Money:{profit}$")
    else:
        drink = MENU[ip]
        if is_resource(drink["ingredients"]):
            payment = insert_coins()
            if is_trans_successful(payment,drink["cost"]):
                make_coffee(ip,drink["ingredients"])








