import tkinter as tk

root = tk.Tk()
root.title('Listboxes')

# Listbox and his scrollbar
lb = tk.Listbox(selectmode='extended', width=50, height=25)
lb.pack(side='left')
sb = tk.Scrollbar(command=lb.yview, width=14)
sb.pack(side='left', fill='y')
lb.config(yscrollcommand=sb.set, selectmode='extended')

e = tk.Entry()
e.pack()

# Interaction buttons
def add_elem():
    lb.insert('end', e.get())

def delete_elem():
    select = list(lb.curselection())
    select.reverse()
    for i in select:
        lb.delete(i)

def save_to_file():
    file = open('list.txt', 'w')
    g = [str(v) for v in lb.get(0, 'end')]
    file.writelines('\n'.join(g))
    file.close()

tk.Button(text='Add', command=add_elem).pack(anchor='n', fill='x')
tk.Button(text='Delete', command=delete_elem).pack(anchor='n', fill='x')
tk.Button(text='Save', command=save_to_file).pack(anchor='n', fill='x')

# Insert initial values
for v in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10):
    lb.insert('end', v)

root.mainloop()
