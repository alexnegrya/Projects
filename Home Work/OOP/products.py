class Product:
    pass

def newProduct(data):
    product = Product()
    product.name = data['name']
    product.price = data['price']
    product.quantity = data['quantity']
    return product

def printProduct(product):
    print(f"{'-'*7} {product.name} {'-'*7}")
    print(f"{product.price} MDL {product.quantity:10}X")
    print('-'*21)

def compareProducts(product1, product2):
    if product1.price > product2.price:
        return product2.name
    elif product1.price < product2.price:
        return product1.name
    else:
        print('The products are the same in price!')

new_1_data = {'name': 'Pizza', 'price': 100, 'quantity': 7}
new_1 = newProduct(new_1_data)
new_2_data = {'name': 'Salad', 'price': 50, 'quantity': 10}
new_2 = newProduct(new_2_data)

print('Products:')
printProduct(new_1)
printProduct(new_2)

print(f"The cheapest product is {compareProducts(new_1, new_2)}.")
