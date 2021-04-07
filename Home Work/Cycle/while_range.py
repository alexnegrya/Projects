start_n = int(input('Enter first number: '))
end_n = int(input('Enter second number: '))

if start_n <= 10 and end_n < start_n:
    while end_n <= start_n:
        print(start_n)
        start_n -= 1
elif end_n <= 10 and start_n < end_n:
    while start_n <= end_n:
        print(start_n)
        start_n += 1
else:
    print('Error!')