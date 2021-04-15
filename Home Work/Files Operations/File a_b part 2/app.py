# function what open file
def fOpen(name, mode):
    f = open(f'./Home Work/Files Operations/File a_b part 2/{name}', mode)
    return f

# create file write data
file = fOpen('in.txt', 'w')
file.write('100 200 300')
file.close()

# remember data to variable {data} in the form of a list
file = fOpen('in.txt', 'r')
read = file.read()
data = read.split()
file.close()

# convert {data} to integer
data[0] = int(data[0])
data[1] = int(data[1])
data[2] = int(data[2])

# math part
num_sum = data[0] + data[1] + data[2]
num_count = len(data)

r = int(num_sum / num_count)

# create file in which remember {r}
file = fOpen('out.txt', 'w')
file.write(str(r))
file.close()

# read [out.txt]
file = fOpen('out.txt', 'r')
read = file.read()

print(f'The average of {data[0]}, {data[1]} and {data[2]} is {read}.')

file.close()
