import tkinter as tk

# Elements classes
class Block:
    def __init__(self, master, func):
        self.ent = tk.Entry(master, width=20)
        self.but = tk.Button(master,
                          text="Преобразовать")
        self.lab = tk.Label(master, width=20,
                         bg='black', fg='white')
        self.but['command'] = getattr(self, func)
        self.ent.pack()
        self.but.pack()
        self.lab.pack()

    def str_to_sort(self):
        s = self.ent.get()
        s = s.split()
        s.sort()
        self.lab['text'] = ' '.join(s)

    def str_reverse(self):
        s = self.ent.get()
        s = s.split()
        s.reverse()
        self.lab['text'] = ' '.join(s)
