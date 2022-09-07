class Product:
    pass


def new_product(data):
    product = Product()
    product.name = data['name']
    product.price = data['price']
    product.quantity = data['quantity']
    return product

def print_product(product):
    print(f"{'-'*7} {product.name} {'-'*7}")
    print(f"{product.price} MDL {product.quantity:10}X")
    print('-'*21)

def compare_products(product1, product2):
    if product1.price > product2.price: return product2.name
    elif product1.price < product2.price: return product1.name
    else: print('The products are the same in price!')


if __name__ == '__main__':
    new_1_data = {'name': 'Pizza', 'price': 100, 'quantity': 7}
    new_1 = new_product(new_1_data)
    new_2_data = {'name': 'Salad', 'price': 50, 'quantity': 10}
    new_2 = new_product(new_2_data)

    print('Products:')
    print_product(new_1)
    print_product(new_2)

    print(f"The cheapest product is {compare_products(new_1, new_2)}.")
