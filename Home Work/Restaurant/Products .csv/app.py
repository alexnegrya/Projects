# define order function
def loadOrder(fileName):
    # create file and {data}
    f = open(f'./Home Work/Restaurant/Products .csv/{fileName}', 'r')
    data = f.readlines()
    f.close()

    # create data variables
    name = []
    price = []
    quantity = []

    # split {data} into {name}, {price} and {quantity}
    for i in data:
        spl = i.split()
        name.append(spl[0])
        price.append(spl[1])
        quantity.append(spl[2])
    
    # print order list
    for n in range(len(name)):
        print(f'{n + 1}) {name[n]:7} {price[n]:7} {quantity[n]}')

    # convert data in {price} and {quantity} to float
    for c in range(len(price)):
        price.append(float(price[c]))
        quantity.append(float(quantity[c]))
    for d in range(2):
        price.pop(d)
        quantity.pop(d)
    price.pop(0)
    quantity.pop(0)

    # calculating and print total cost
    totalCost = 0
    for t in range(len(price)):
        price[t] *= quantity[t]
        totalCost += price[t]
    print(f'\nTotal cost: {totalCost}')

# call order function
loadOrder('order.csv')
