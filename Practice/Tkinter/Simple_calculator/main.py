import tkinter as tk

def is_dot_in_str(string):
    for letter in string:
        if letter == '.':
            return True
    return False

def add():
    # getting inputs
    a = number1.get()
    b = number2.get()
    try:
        # check if dot in inputs
        if is_dot_in_str(a):
            a = float(a)
        else:
            a = int(a)
        if is_dot_in_str(b):
            b = float(b)
        else:
            b = int(b)
    except:
        res['text'] = 'Error!'
    else:
        # calculating and editing result label text
        res['text'] = a + b

def sub():
    # getting inputs
    a = number1.get()
    b = number2.get()
    try:
        # check if dot in inputs
        if is_dot_in_str(a):
            a = float(a)
        else:
            a = int(a)
        if is_dot_in_str(b):
            b = float(b)
        else:
            b = int(b)
    except:
        res['text'] = 'Error!'
    else:
        # calculating and editing result label text
        res['text'] = a - b

def mul():
    # getting inputs
    a = number1.get()
    b = number2.get()
    try:
        # check if dot in inputs
        if is_dot_in_str(a):
            a = float(a)
        else:
            a = int(a)
        if is_dot_in_str(b):
            b = float(b)
        else:
            b = int(b)
    except:
        res['text'] = 'Error!'
    else:
        # calculating and editing result label text
        res['text'] = a * b

def div():
    # getting inputs
    a = number1.get()
    b = number2.get()
    try:
        # check if dot in inputs
        if is_dot_in_str(a):
            a = float(a)
        else:
            a = int(a)
        if is_dot_in_str(b):
            b = float(b)
        else:
            b = int(b)
    except:
        res['text'] = 'Error!'
    else:
        # calculating and editing result label text
        res['text'] = a / b

# Main window
root = tk.Tk()

# Entries
number1 = tk.Entry(width=10)
number2 = tk.Entry(width=10)

# Buttons
add_btn = tk.Button(command=add, text='+', width=12)
sub_btn = tk.Button(command=sub, text='-', width=12)
mul_btn = tk.Button(command=mul, text='*', width=12)
div_btn = tk.Button(command=div, text='/', width=12)

# Result label
res = tk.Label(width=18)

# Packing
number1.pack()
number2.pack()
add_btn.pack()
sub_btn.pack()
mul_btn.pack()
div_btn.pack()
res.pack()

# Starting app
root.mainloop()
