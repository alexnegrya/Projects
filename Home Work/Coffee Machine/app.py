from coffee import *

machine_1 = CoffeeMachine('Sony')
coffee_1 = machine_1.makeCoffee('Espresso', {'water': '125ml', 'sugar': '3g'})

machine_2 = CoffeeMachine('LG')
coffee_2 = machine_2.makeCoffee('Cappuccino', {'water': '110ml', 'sugar': '2g'})

machine_3 = CoffeeMachine('Philips')
coffee_3 = machine_3.makeCoffee('Robusta', {'water': '115ml', 'sugar': '2.5g'})

print(coffee_1)
print()
print(coffee_2)
print()
print(coffee_3)