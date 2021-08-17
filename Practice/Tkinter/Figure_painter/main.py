import tkinter as tk

# Main window
root = tk.Tk()
root.title('Figures painter')

# Canavas with user figures
c = tk.Canvas(width=400, height=400, bg='white')
c.pack()

# Draw figure functional
def add_figure():
    w = tk.Toplevel()
    w.title('Figure')
    w.minsize(200, 100)
    w.resizable(False, False)

    # first coords
    tk.Label(w).grid(row=0, column=0, padx=20)
    tk.Label(w, text='x1').grid(row=0, column=1)
    x1 = tk.Entry(w, width=3)
    x1.grid(row=0, column=2)
    tk.Label(w).grid(row=0, column=3, padx=10)
    tk.Label(w, text='y1').grid(row=0, column=4)
    y1 = tk.Entry(w, width=3)
    y1.grid(row=0, column=5)
    tk.Label(w).grid(row=0, column=6, padx=20)

    # second coords
    tk.Label(w).grid(row=1, column=0, padx=20)
    tk.Label(w, text='x2').grid(row=1, column=1)
    x2 = tk.Entry(w, width=3)
    x2.grid(row=1, column=2)
    tk.Label(w).grid(row=1, column=3, padx=10)
    tk.Label(w, text='y2').grid(row=1, column=4)
    y2 = tk.Entry(w, width=3)
    y2.grid(row=1, column=5)
    tk.Label(w).grid(row=1, column=6, padx=20)

    # radiobuttons
    var = tk.BooleanVar()
    tk.Radiobutton(w, text='Rectangle', variable=var, value=True)\
        .grid(row=2, column=2, sticky='w', columnspan=4)
    tk.Radiobutton(w, text='Oval', variable=var, value=False)\
        .grid(row=3, column=2, sticky='w', columnspan=4)

    # draw button
    def draw_figure():
        count = 0
        coords = (int(x1.get()), int(y1.get()), int(x2.get()), int(y2.get()))
        for v in coords:
            if v != '':
                count += 1
        if count == 4:
            if var.get() == True:
                c.create_rectangle(coords[0], coords[1],
                 coords[2], coords[3], outline='black', width=2)
            elif var.get() == False:
                c.create_oval(coords[0], coords[1],
                 coords[2], coords[3], outline='black', width=2)
            w.destroy()
    tk.Button(w, text='Draw', command=draw_figure).grid(row=4, columnspan=7)


# Draw figure button
tk.Button(text='Add figure', command=add_figure).pack()

# Starting app
root.mainloop()
