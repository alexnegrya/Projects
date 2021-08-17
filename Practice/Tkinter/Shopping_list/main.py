import tkinter as tk

root = tk.Tk()
root.title('Shopping list manager')

# Functions
def move_right():
    selected = list(prodlist.curselection())
    selected.reverse()
    for i in selected:
        shoplist.insert('end', prodlist.get(i))
        prodlist.delete(i)

def move_left():
    selected = list(shoplist.curselection())
    selected.reverse()
    for i in selected:
        prodlist.insert('end', shoplist.get(i))
        shoplist.delete(i)

# List of products
prodlist = tk.Listbox(selectmode='extended')
prodlist.pack(side='left')
prods = ('bananas', 'apples', 'carrot', 'bread', 'butter', 'meat', 'potato')
for prod in prods:
    prodlist.insert('end', prod)

# Move buttons
b_frame = tk.Frame()
b_frame.pack(side='left', expand=1)
m_right = tk.Button(b_frame, text='>>>', command=move_right)
m_right.pack()
m_left = tk.Button(b_frame, text='<<<', command=move_left)
m_left.pack()

# Shopping list
shoplist = tk.Listbox(selectmode='extended')
shoplist.pack(side='left')

# Starting app
root.mainloop()
