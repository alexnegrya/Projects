import tkinter as tk

root = tk.Tk()
root.title('Text mover')

# Functions
def to_list(event):
    l.insert('end', t.get())
    t.delete(0, 'end')

def to_text(event):
    t.delete(0, 'end')
    try:
        t.insert(0, l.selection_get())
    except tk.TclError:
        pass
    selected = l.curselection()
    if len(selected) != 0:
        l.delete(selected[0])

# Text widget
t_frame = tk.LabelFrame(text='Text')
t_frame.pack()
t = tk.Entry(t_frame, width=45)
t.pack()
t.bind('<Return>', to_list)

# List widget
l_frame = tk.LabelFrame(text='List')
l_frame.pack()
l = tk.Listbox(l_frame, width=45, height=25)
l.pack()
l.bind('<Double-Button-1>', to_text)

# Starting app
root.mainloop()

