import tkinter as tk

root = tk.Tk()
root.minsize(500, 500)
root.title('Make something')

def b1(event):
    root.title('Left button was pressed')

def b2(event):
    root.title('Mouse wheel was pressed')

def b3(event):
    root.title('Right button was pressed')

root.bind('<Button-1>', b1)
root.bind('<Button-2>', b2)
root.bind('<Button-3>', b3)

def move(event):
    root.title(f'Mouse move {event.x}x{event.y}')

root.bind('<Motion>', move)

root.mainloop()
