start_n = int(input('Enter first number: '))
end_n = int(input('Enter second number: '))

print()
if end_n < start_n:
    while end_n <= start_n:
        print(start_n)
        start_n -= 1
elif start_n < end_n:
    while start_n <= end_n:
        print(start_n)
        start_n += 1
else: print(start_n)
