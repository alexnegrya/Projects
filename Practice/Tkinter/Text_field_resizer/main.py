import tkinter as tk

root = tk.Tk()
root.title('Text field resizer')

# Size controller frame
controller = tk.Frame()

# Input fields frame
fields = tk.Frame(controller)

# Width input field
width = tk.Entry(fields, width=4)

# Height input field
height = tk.Entry(fields, width=4)

# Change button
def change_size(event):
    text['width'] = int(width.get())
    text['height'] = int(height.get())

change = tk.Button(controller, text='Change', command=lambda e=None: change_size(event=e))

# Text field
def change_color(event):
    global text
    if str(event.type) == '9': # focus in
        text['bg'] = 'white'
    elif str(event.type) == '10': # focus out
        text['bg'] = 'lightgrey'

text = tk.Text()

text.bind('<FocusIn>', change_color)
text.bind('<FocusOut>', change_color)

# Binding
width.bind('<Return>', change_size)
height.bind('<Return>', change_size)

# Packing
controller.pack()
fields.pack(side='left')
width.pack()
height.pack()
change.pack(side='left')
text.pack(side='bottom')

# Starting app
root.mainloop()
