a = int(input('Enter first number: '))
op = input('Enter the operator: ')
b = int(input('Enter the second number: '))

if op == '+':
    c = a + b
    print(a,op,b,'=',c),
elif op == '-':
    c = a - b
    print(a,op,b,'=',c),
elif op == '*':
    c = a * b
    print(a,op,b,'=',c),
elif op == '/':
    c = a / b
    print(a,op,b,'=',c),
else:
    print('Unsuccesfully')