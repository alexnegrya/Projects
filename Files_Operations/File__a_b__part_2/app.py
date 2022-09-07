# create file write data
file = open('in.txt', 'w')
file.write('100 200 300')
file.close()

# remember data to variable {data} in the form of a list
file = open('in.txt', 'r')
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
file = open('out.txt', 'w')
file.write(str(r))
file.close()

# read [out.txt]
file = open('out.txt', 'r')
read = file.read()

print(f'The average of {data[0]}, {data[1]} and {data[2]} is {read}.')

file.close()
