import tkinter as tk
from tkinter.constants import END, CENTER

# Functions
def get_red_code():
    # edit label text
    color['text'] = 'red'
    # edit entry text
    color_code.delete(0, END)
    color_code.insert(0, red['bg'])

def get_orange_code():
    # edit label text
    color['text'] = 'orange'
    # edit entry text
    color_code.delete(0, END)
    color_code.insert(0, orange['bg'])

def get_yellow_code():
    # edit label text
    color['text'] = 'yellow'
    # edit entry text
    color_code.delete(0, END)
    color_code.insert(0, yellow['bg'])

def get_green_code():
    # edit label text
    color['text'] = 'green'
    # edit entry text
    color_code.delete(0, END)
    color_code.insert(0, green['bg'])

def get_light_blue_code():
    # edit label text
    color['text'] = 'light blue'
    # edit entry text
    color_code.delete(0, END)
    color_code.insert(0, light_blue['bg'])

def get_blue_code():
    # edit label text
    color['text'] = 'blue'
    # edit entry text
    color_code.delete(0, END)
    color_code.insert(0, blue['bg'])

def get_violet_code():
    # edit label text
    color['text'] = 'violet'
    # edit entry text
    color_code.delete(0, END)
    color_code.insert(0, violet['bg'])

# Main window
root = tk.Tk()

# Color name label
color = tk.Label(width=14)
color.pack(expand=1)

# Color code entry
color_code = tk.Entry(width=14, justify=CENTER, textvariable=tk.StringVar())
color_code.pack(pady=4)

# Colors buttons
red = tk.Button(bg='#ff0000', activebackground='red3',
 command=get_red_code)
red.pack(side='left')
orange = tk.Button(bg='#ff7d00', activebackground='orange3',
 command=get_orange_code)
orange.pack(side='left')
yellow = tk.Button(bg='#ffff00', activebackground='yellow3',
 command=get_yellow_code)
yellow.pack(side='left')
green = tk.Button(bg='#00ff00', activebackground='green3',
 command=get_green_code)
green.pack(side='left')
light_blue = tk.Button(bg='#007dff', activebackground='steel blue',
 command=get_light_blue_code)
light_blue.pack(side='left')
blue = tk.Button(bg='#0000ff', activebackground='medium blue',
 command=get_blue_code)
blue.pack(side='left')
violet = tk.Button(bg='#7d00ff', activebackground='purple3',
 command=get_violet_code)
violet.pack(side='left')

# Starting app
root.mainloop()
