import json

def load(fileName):
    file = open( f"Home Work/Food Order/data/{fileName}.json", "r" )
    data = json.loads(file.read())
    return data

def save(fileName, data):
    file = open( f"Home Work/Food Order/data/{fileName}.json", "w" )
    file.write(json.dumps(data))
    file.close()


# structName - order
def billSave(fileName, structName):
    file = open(f'Home Work/Food Order/data/{fileName}.txt', 'w')
    file.write('#'*34+'\n')
    file.write(
        f"Total price:\t\t {structName['total']['amount']:9} {structName['total']['currency']:9}"+'\n'
        )
    file.write('#'*34)

def billPrint(structName):
    print('#'*35)
    print(
        'Total price:\t\t', f" {structName['total']['amount']:5} {structName['total']['currency']:6}"
        )
    print('#'*35)
