from math import ceil

products = [
    {'name': 'Salad', 'price': 25.00 },
    {'name': 'Soup',  'price': 15.00 },
    {'name': 'Bread', 'price': 5.00  },
    {'name': 'Kebab', 'price': 50.00 },
    {'name': 'Pizza', 'price': 100.00},
]

# ############################# search max #########################################
# max_i = 0
# for i in range(len(products)):
#     if products[i]['price'] > products[max_i]['price']:
#         max_i = i

# print( f'{max_i} > {products[max_i]["name"]:25} {products[max_i]["price"]:7} MDL' )
# ##################################################################################

# ######### search by product name #############
# product_name = 'Kebab'
# result = ''
# pos = 0
# price = 0

# for i in range(len(products)):
#     if product_name in products[i]['name']:
#         result = products[i]['name']
#         price = products[i]['price']
#         pos = i
#         break

# print( f'{pos} > {result:6} {price} MDL' )
# ##############################################

# ############# SIMPLE PAGINATION ##############
# data
item_count   = len(products)
page_current = 1
per_page     = 2
pages_total  = ceil( item_count / per_page )
page_min     = pages_total - pages_total

while True:
    # math
    start_index  = (page_current - 1) * per_page
    end_index    = start_index + per_page

    # list of products
    for i in range(item_count):
        if i >= start_index and i < end_index:
            print( f'{i} > {products[i]["name"]:25} {products[i]["price"]:7} MDL' )

    # pages
    print()

    for page in range(1, pages_total + 1):
        if page == page_current:
            print('[',page,']', end=' ')
        else:
            print(page, end=' ')
            
    print()

    # controls
    option = input('>>  ')
    
    if option == '<':
        page_current -= 1
        if page_current <= page_min:
            page_current = 1
    elif option == '>':
        page_current += 1
        if page_current > pages_total:
            page_current = pages_total
    elif option == 'exit':
        break
# ##############################################
