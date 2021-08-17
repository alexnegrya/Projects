import tkinter as tk

root = tk.Tk()
root.title('Move your mouse')
root.minsize(500, 500)

show_direction = False

c = tk.Canvas(width=500, height=500, bg='grey')
c.pack()
c.focus_set()

# NNE and SSW line
c.create_line(375, 0, 125, 500, width=2, fill='grey40')
# ENE and WSW line
c.create_line(500, 125, 0, 375, width=2, fill='grey40')
# ESE and WNW line
c.create_line(500, 375, 0, 125, width=2, fill='grey40')
# SSE and NNW line
c.create_line(375, 500, 125, 0, width=2, fill='grey40')

# diagonal right line
c.create_line(0, 0, 500, 500, width=3, fill='grey20')
# diagonal left line
c.create_line(0, 500, 500, 0, width=3, fill='grey20')

# vertical line
c.create_line(250, 0, 250, 500, width=5)
# horisontal line
c.create_line(0, 250, 500, 250, width=5)


def getClickDirection(event):
    for y in range(500):
        for x in range(500):
            # Center
            if x == 250 and y == 250 and (event.x, event.y) == (x, y):
                return 'Center'
            # N
            elif x == 250 and y < 250 and (event.x, event.y) == (x, y):
                return 'N'
            # E
            elif x > 250 and y == 250 and (event.x, event.y) == (x, y):
                return 'E'
            # S
            elif x == 250 and y > 250 and (event.x, event.y) == (x, y):
                return 'S'
            # W
            elif x < 250 and y == 250 and (event.x, event.y) == (x, y):
                return 'W'
            # NE/NNE/ENE
            elif x > 250 and y < 250 and (event.x, event.y) == (x, y):
                if x + y == 500:
                    return 'NE'
                elif x + y <= 498:
                    return 'NNE'
                elif x + y > 500 and x + y <= 748:
                    return 'ENE'
            # SE/ESE/SSE
            elif x > 250 and y > 250 and (event.x, event.y) == (x, y):
                if x == y:
                    return 'SE'
                elif x + y <= 998:
                    if x > y:
                        return 'ESE'
                    elif x < y:
                        return 'SSE'
            # SW/SSW/WSW
            elif x < 250 and y > 250 and (event.x, event.y) == (x, y):
                if x + y == 500:
                    return 'SW'
                elif x + y > 500 and x + y <= 748:
                    return 'SSW'
                elif x + y <= 498:
                    return 'WSW'
            # NW/WNW/NNW
            elif x < 250 and y < 250 and (event.x, event.y) == (x, y):
                if x == y:
                    return 'NW'
                elif x + y <= 498:
                    if x < y:
                        return 'WNW'
                    elif x > y:
                        return 'NNW'

c.bind('<Button-1>', lambda event: print(getClickDirection(event)))


def showCoords(event):
    global show_direction
    if show_direction == False:
        root.title(f'{event.x}x{event.y}; {event.x+event.y}')
    elif show_direction:
        root.title(f'{event.x}x{event.y}; {event.x+event.y}; {getClickDirection(event)}')

root.bind('<Motion>', showCoords)


def showDirection(event):
    if len(root.title()) <= 12:
        root.title(root.title() + f'; {getClickDirection(event)}')
    else:
        new_title = root.title()
        separators = 0
        for i in range(len(new_title)):
            if new_title[i] == ';':
                separators += 1
            if separators == 3:
                new_title[i] = ''
        root.title(new_title)

c.bind('<Button-3>', showDirection)

def setDirectionShowing(event):
    global show_direction
    if show_direction == True:
        show_direction = False
    elif show_direction == False:
        show_direction = True

c.bind('<Double-Button-3>', setDirectionShowing)


# tk.Label first or int later if tuple_mode is True
l = None
# geo direction (str)
direction = None
# tk.Canvas object (oval)
ball = None
# False if direction is wrong or True if direction is correct
start_mv = False
# True or False in dependence ball currently moves or not
moving = False
def startTest(event):
    global l
    global direction
    global ball
    global moving

    if moving == False:
        if type(l) == tk.Label:
            l.destroy()
        if direction != None:
            direction.destroy()
        if ball != None:
            c.delete(ball)

    def start(event, direction, label, xm=None, ym=None):
        global ball
        global start_mv
        global l
        global moving
        
        if moving == False:
            if xm == None and ym == None:
                if start_mv == False:
                    # geo directions
                    directions = ('N', 'E', 'S', 'W',
                                'NE', 'SE', 'SW', 'NW',
                                'NNE', 'ENE', 'ESE', 'SSE', 'SSW', 'WSW', 'WNW', 'NNW')
                    # geo direction
                    gd = direction.get().upper()
                    label.destroy()
                    direction.destroy()
                    direction = gd
                    if len(gd) < 1 or len(gd) > 3:
                        len_error = tk.Label(text='Wrong direction!')
                        len_error.pack()
                        root.after(1500, len_error.destroy)
                        c.focus_set()
                    elif gd not in directions:
                        exists_error = tk.Label(
                            text='This direction does not exists!')
                        exists_error.pack()
                        root.after(1500, exists_error.destroy)
                        c.focus_set()
                    else:
                        ball = c.create_oval(240, 240, 260, 260, fill='grey80')
                        start_mv = True

                if start_mv:
                    if type(direction) == tk.Entry:
                        direction = direction.get().upper()
                    if len(direction) == 3:
                        if direction == 'NNE':
                            xm = (0, 1)
                            ym = (-1, 0)
                        elif direction == 'ENE':
                            xm = (1, 0)
                            ym = (0, -1)
                        elif direction == 'ESE':
                            xm = (1, 0)
                            ym = (0, 1)
                        elif direction == 'SSE':
                            xm = (0, 1)
                            ym = (1, 0)
                        elif direction == 'SSW':
                            xm = (0, -1)
                            ym = (1, 0)
                        elif direction == 'WSW':
                            xm = (-1, 0)
                            ym = (0, 1)
                        elif direction == 'WNW':
                            xm = (-1, 0)
                            ym = (0, -1)
                        elif direction == 'NNW':
                            xm = (0, -1)
                            ym = (-1, 0)
                    elif len(direction) == 2:
                        if direction == 'NE':
                            xm = 1
                            ym = -1
                        elif direction == 'SE':
                            xm = 1
                            ym = 1
                        elif direction == 'SW':
                            xm = -1
                            ym = 1
                        elif direction == 'NW':
                            xm = -1
                            ym = -1
                    elif len(direction) == 1:
                        if direction == 'N':
                            xm = 0
                            ym = -1
                        elif direction == 'E':
                            xm = 1
                            ym = 0
                        elif direction == 'S':
                            xm = 0
                            ym = 1
                        elif direction == 'W':
                            xm = -1
                            ym = 0
                    root.after(10,
                            lambda e=event, d=direction, l=None, x=xm, y=ym: start(e, d, l, x, y))
                    moving = True
        elif moving and xm != None and ym != None:
            int_mode = 0
            tuple_mode = 0
            if c.coords(ball)[0] == 0 or c.coords(ball)[1] == 0\
                    or c.coords(ball)[2] == 500 or c.coords(ball)[3] == 500:
                int_mode = False
                tuple_mode = False
            if type(int_mode) == int and type(tuple_mode) == int:
                for obj in (xm, ym):
                    if type(obj) == int:
                        int_mode += 1
                    elif type(obj) == tuple:
                        tuple_mode += 1
                if int_mode == 2 and tuple_mode == 0:
                    int_mode = True
                    tuple_mode = False
                elif tuple_mode == 2 and int_mode == 0:
                    tuple_mode = True
                    int_mode = False

            if int_mode:
                c.move(ball, xm, ym)
                c.update()
                root.after(10,
                        lambda e=event, d=direction, l=None, x=xm, y=ym: start(e, d, l, x, y))
            # ----- Tuple mode -----
            # Round 1: xm = xm[0]; ym = ym[0] (repeat 2 times)
            # Round 2: xm = xm[1]; ym = ym[1] (repeat 1 time)
            # l = 0 -- Round 1
            # l = 1 -- Round 1
            # l = 2 -- Round 2; l = 0
            elif tuple_mode:
                if type(l) != int:
                    l = 0
                if l == 0:
                    c.move(ball, xm[0], ym[0])
                    c.update()
                    l = 1
                    root.after(10,
                            lambda e=event, d=direction, l=l, x=xm, y=ym: start(e, d, l, x, y))
                elif l == 1:
                    c.move(ball, xm[0], ym[0])
                    c.update()
                    l = 2
                    root.after(10,
                            lambda e=event, d=direction, l=l, x=xm, y=ym: start(e, d, l, x, y))
                elif l == 2:
                    c.move(ball, xm[1], ym[1])
                    c.update()
                    l = 0
                    root.after(10,
                            lambda e=event, d=direction, l=l, x=xm, y=ym: start(e, d, l, x, y))
            else:
                start_mv = False
                moving = False
                c.focus_set()

    if moving == False:
        l = tk.Label(text='Enter direction')
        l.pack()
        direction = tk.Entry()
        direction.pack()
        direction.focus_set()
        direction.bind('<Return>', lambda e, d=direction,
                    label=l: start(e, d, label))
        direction.bind('<Escape>', lambda e: [obj.destroy() for obj in (l, direction)] and c.focus_set())

c.bind('<Button-2>', startTest)
c.bind('<Return>', startTest)


def destroyTestWidgets(event):
    for obj in (l, direction):
        if obj != None:
            obj.destroy()

c.bind('<Escape>', destroyTestWidgets)

root.mainloop()
