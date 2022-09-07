import json


def load(file_name: str):
    file = open(f"data/{file_name}.json", "r")
    data = json.loads(file.read())
    return data

def save(file_name: str, data):
    file = open(f"data/{file_name}.json", "w")
    file.write(json.dumps(data))
    file.close()


# struct_name - order
def save_bill(file_name, struct_name):
    file = open(f'data/{file_name}.txt', 'w')
    file.write('#'*34+'\n')
    file.write(f"Total price:\t\t {struct_name['total']['amount']:9}" +
        f" {struct_name['total']['currency']:9}"+'\n')
    file.write('#'*34)

def print_bill(struct_name):
    print('#'*35)
    print('Total price:\t\t', f"{struct_name['total']['amount']:5}",
        f"{struct_name['total']['currency']:6}")
    print('#'*35)
