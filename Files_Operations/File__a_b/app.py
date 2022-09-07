# function for open file
def fopen(mode):
    f = open('in.txt', mode)
    return f

# write in file 100 200
file = fopen('w')
file.write('100 200')
file.close()

# math part
file = fopen('r')

a = int(file.readline(4))
b = int(file.readline(3))

r = a + b

# print result
print('Result is:', r)
