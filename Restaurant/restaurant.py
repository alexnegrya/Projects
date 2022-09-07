# Food 1
food_1_name      = 'Pizza'
food_1_price     = 100   
food_1_available = 50

# Food 2
food_2_name = 'Soup'
food_2_price = 70
food_2_available = 100

# Delivery cost
delivery_cost = 150

# User choice
print('Welcome to out restourant! Here is a menu:')
print('1)',food_1_name)
print('2)',food_2_name)
user_choice = int(input('Write the number of the food you want to order: '))

# Calcucations
if user_choice == 1: # If user choise is food number 1
    food_1_quantity  = int(input('How many ' + food_1_name + ' do you want? '))
    food_1_cost = food_1_quantity * food_1_price
    if food_1_quantity < 1:
        print("Order at least one of the menu items!")
    elif food_1_quantity > food_1_available:
        print("So much food is out of stock!")
    delivery = str(input('Do you need delivery? Write Yes or No: ')) # Delivery
    if delivery == "Yes" and food_1_cost > 1000:
        print('You have ordered',food_1_quantity,'x',food_1_name,'=',food_1_cost),
    elif delivery == 'Yes' and food_1_cost <= 1000:
        food_1_final_cost = food_1_cost + delivery_cost
        print('You have ordered',food_1_quantity,'x',food_1_name,'=',food_1_final_cost),
    elif delivery == 'No':
        print('You have ordered',food_1_quantity,'x',food_1_name,'=',food_1_cost),
    else:
        print('Write to the question about the delivery of the answer Yes or No!')
elif user_choice == 2: # If user choise is food number 2
    food_2_quantity  = int(input('How many ' + food_2_name + ' do you want? '))
    food_2_cost = food_2_quantity * food_2_price
    if food_2_quantity < 1:
        print("Order at least one of the menu items!")
    elif food_2_quantity > food_2_available:
        print("So much food is out of stock!")
    delivery = str(input('Do you need delivery? Write Yes or No: ')) # Delivery
    if delivery == "Yes" and food_2_cost > 1000:
        print('You have ordered',food_2_quantity,'x',food_2_name,'=',food_2_cost),
    elif delivery == 'Yes' and food_2_cost <= 1000:
        food_2_final_cost = food_2_cost + delivery_cost
        print('You have ordered',food_2_quantity,'x',food_2_name,'=',food_2_final_cost),
    elif delivery == 'No':
        print('You have ordered',food_2_quantity,'x',food_2_name,'=',food_2_cost),
    else:
        print('Write to the question about the delivery of the answer Yes or No!')
else:
    print('Enter the number that indicates the food you selected in the menu!')
