def getData( index ):
  data = [10,20,30,40,50]
  return data[index]

print('Situation A')
try:
    # Situation A
    index = int(input("Enter an index: "))
    print(getData(index))
except ValueError:
    print("index cannot be something else than an integer")
except IndexError:
    print("an index value cannot be outside the list")

print('Situation B')
try:
    # Situation B
    index = 1000
    print(getData(index))
except IndexError:
    print("an index value cannot be outside the list")
