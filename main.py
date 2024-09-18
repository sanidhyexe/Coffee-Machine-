import art
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
is_on = True

def can_make_drink(drink):
    can_make = True
    for item in resources:
        if not MENU[drink]['ingredients'][item] <= resources[item]:
            can_make = False
    return can_make

def payment():
    print("Enter the quantity of money as comfortable... ")
    quarters = int(input("Enter the number of quarters (1 quarters = $0.25) : "))
    dimes = int(input("Enter the number of dimes (1 dimes = $0.10) : "))
    nickles = int(input("Enter the number of nickles (1 nickles = $0.05) : "))
    pennies = int(input("Enter the number of pennies (pennies = $0.01) : "))
    total_amount_recieved = 0.25*quarters + 0.10*dimes + 0.05*nickles + 0.01*pennies
    return total_amount_recieved



while is_on:
    choice = input('What would you like? (espresso/latte/cappuccino): ').lower()
    if choice not in MENU and choice!= 'off' and choice!='report':
        print("Invalid choice. Please try again.")
        continue
    elif choice == 'off':
        print('Thanks for using us. :)')
        is_on = False
    elif choice == 'report':
        print(f"Milk : {resources['milk']} ml")
        print(f"Water : {resources['water']} ml")
        print(f"Coffee : {resources['coffee']} g")
        print(f"Money : {profit} $")
    elif choice == 'espresso' or choice == 'cappuccino' or choice == 'latte':
        print(f"You ordered a {choice} ���️")
        if can_make_drink(choice):
            print(f"Your {choice} would be {MENU[choice]['cost']}$")
            paid_amount = payment()
            amount = abs(paid_amount - MENU[choice]['cost'])
            if amount > 0 and paid_amount < MENU[choice]['cost']:
                print("Sorry that was not sufficient to pay the amount. Money Refunded !!")
                is_on = False
            elif amount > 0 and paid_amount > MENU[choice]['cost']:
                print(f"Here is your {choice} ���️, enjoy!")
                print(f"Returning change: {amount:.2f} $")
            elif amount == 0 and paid_amount == MENU[choice]['cost']:
                print(f"Here is your {choice} ���️, enjoy!")
            print(art.art['coffee'])
            for items in resources:
                resources[items] -= MENU[choice]['ingredients'][items]
            profit += MENU[choice]['cost']

        else:
            print("Sorry, we are out of that ingredient. Please try again later.")
            is_on = False


