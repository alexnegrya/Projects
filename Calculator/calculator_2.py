a = int(input('Enter first number: '))
op = input('Enter the operator: ')
b = int(input('Enter the second number: '))

c = None
try:
    if op == '+': c = a + b
    elif op == '-': c = a - b
    elif op == '*': c = a * b
    elif op == '/': c = a / b
    elif op == '//': c = a // b
    elif op == '%': c = a % b
    elif op == '**': c = a ** b
except ValueError as e: raise SystemExit(str(e)[0].upper() + str(e)[1:])

print(a, op, b, '=', c) if c != None else print('Unknown operation')
