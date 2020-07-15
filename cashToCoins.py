dollarAmount = 8.69

piggyBank = {
    "pennies": 0,
    "nickels": 0,
    "dimes": 0,
    "quarters": 0
}

# Your magic Python code here

def cash_to_coins(money, bank):
    bank["quarters"] = int(money / .25)
    money = money - bank["quarters"] * .25
    bank["dimes"] = int(money / .10)
    money = money - bank["dimes"] * .10
    bank["nickels"] = int(money / .05)
    money = money - bank["nickels"] * .05
    bank["pennies"] = round(money / .01)

cash_to_coins(dollarAmount, piggyBank)

print(piggyBank)


