import tkinter as tk

root = tk.Tk()
root.title('Contacts')

# Contacts frame
contacts = tk.Frame()
contacts.pack(side='left', fill='y')

# Variable
var = tk.IntVar()
var.set(-1)

# Show number function
l = tk.Label()
l.pack(padx=100)
def showNumber():
    global l
    l.destroy()
    if var.get() == 0:
        l = tk.Label(text=c1.number)
    elif var.get() == 1:
        l = tk.Label(text=c2.number)
    elif var.get() == 2:
        l = tk.Label(text=c3.number)
    l.pack(anchor='w', expand=1, padx=100)

# Contacts
c1 = tk.Radiobutton(contacts, indicatoron=0, text='Grisha', variable=var, value=0)
c1.config(command=showNumber, width=10, height=5)
c1.number = '+758152940'
c2 = tk.Radiobutton(contacts, indicatoron=0, text='Kolya', variable=var, value=1)
c2.config(command=showNumber, width=10, height=5)
c2.number = '+318456980'
c3 = tk.Radiobutton(contacts, indicatoron=0, text='Katya', variable=var, value=2)
c3.config(command=showNumber, width=10, height=5)
c3.number = '+984686222'
c1.pack()
c2.pack()
c3.pack()

root.mainloop()
