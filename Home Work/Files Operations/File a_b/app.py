# function for open file
def fOpen(mode):
    f = open('./Home Work/Files Operations/File a_b/in.txt', mode)
    return f

# write in file 100 200
file = fOpen('w')
file.write('100 200')
file.close()

# math part
file = fOpen('r')

a = int(file.readline(4))
b = int(file.readline(3))

r = a + b

# print result
print('Result is:', r)
