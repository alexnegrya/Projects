import tkinter as tk
from tkinter import messagebox as mb
from tkinter import filedialog as fd

# Main window
root = tk.Tk()

# Text field
text = tk.Text(width=50, height=25)
text.pack()
text.focus_set()

# Buttons frame
frame = tk.Frame()
frame.pack()

# Open file button
def open_file():
    filename = fd.askopenfilename()
    if type(filename) != tuple and filename != '':
        file = open(filename, 'r')
        text.delete(1.0, 'end')
        text.insert(1.0, file.read())
        file.close()
    text.focus_set()
tk.Button(frame, text='Open', command=open_file).pack(side='left')

# Save file button
def save_file():
    filename = fd.asksaveasfilename()
    if type(filename) != tuple and filename != '':
        file = open(filename, 'w')
        file.write(text.get(1.0, 'end'))
        file.close()
    text.focus_set()
tk.Button(frame, text='Save', command=save_file).pack(side='left')

# Clear button
def clear():
    answer = mb.askyesno('Clear all', 'You are sure')
    if answer:
        text.delete(1.0, 'end')
    text.focus_set()
tk.Button(text='Clear all', command=clear).pack()

# Binds
text.bind('<Control-o>', lambda event: open_file())
text.bind('<Control-s>', lambda event: save_file())
text.bind('<Control-x>', lambda event: clear())

# Starting app
root.mainloop()
