import tkinter as tk

root = tk.Tk()
root.title('Home')

c = tk.Canvas(width=500, height=500)
c.pack()

c.create_oval(350, 50, 450, 150, fill='orange1', outline='orange1')
c.create_polygon(100, 275, 400, 275, 250, 150, fill='red2', outline='red2')
c.create_rectangle(110, 276, 390, 426, fill='DarkGoldenrod3', outline='DarkGoldenrod3')

x1 = 10
x2 = 100
for v in range(24):
    c.create_arc(x1, 400, x2, 604, style='arc', start=180, extent=-60, width=5, outline='green')
    x1 += 20
    x2 += 20

root.mainloop()
