import tkinter as tk

# Functions
def open_file():
    try:
        f = open(file.get(), 'r')
    except:
        f = open(file.get(), 'w')
        f.write('')
        f.close()
        f = open(file.get(), 'r')
    text.insert(1.0, f.read())
    f.close()

def save_file():
    f = open(file.get(), 'w+')
    f.write(text.get(1.0, 'end'))
    f.close()

# Main window
root = tk.Tk()
root.title('File editor')

# Menu frame
menu = tk.Frame()
menu.pack(fill='x')

# File name entry
file = tk.Entry(menu)
file.pack(side='left')

# Open file button
o_file = tk.Button(menu, text='Open', command=open_file)
o_file.pack(side='right')

# Save file button
s_file = tk.Button(menu, text='Save', command=save_file)
s_file.pack(side='right')

# File text field
text = tk.Text()
text.pack(fill='both')

# Starting app
root.mainloop()
