import tkinter as tk

root = tk.Tk()
root.title('Canvases 2')
root.minsize(500, 500)

def mouse_motion(event):
    root.title(f'{event.x}x{event.y}; sum = {event.x + event.y}')

root.bind('<Motion>', mouse_motion)

c = tk.Canvas(width=500, height=500)
c.pack()

# returns mouse click direction or None if clicked on the border
def getClickDirection(event, obj_center_coords=None):
    # checking object center coords
    if obj_center_coords != None:
        if type(obj_center_coords) not in (list, tuple):
            raise TypeError('object center coordinates must be in tuple or in list')
        else:
            if type(obj_center_coords) == list:
                obj_center_coords == tuple(obj_center_coords)
            if len(obj_center_coords) != 2:
                raise ValueError('must be transmitted only 2 coordinates: x and y')
            for v in obj_center_coords:
                if type(v) != int:
                    raise TypeError('coordinates must be int type')

    # click direction relative to the window
    if obj_center_coords == None:
        xc = 250
        yc = 250
        s = 500
    # click direction relative to the object
    elif obj_center_coords != None:
        xc = obj_center_coords[0]
        yc = obj_center_coords[1]
        s = xc + yc

    for y in range(500):
        for x in range(500):
            # Center
            if x == xc and y == yc and (event.x, event.y) == (x, y):
                return 'Center'
            # N
            elif x == xc and y < yc and (event.x, event.y) == (x, y):
                return 'N'
            # E
            elif x > xc and y == yc and (event.x, event.y) == (x, y):
                return 'E'
            # S
            elif x == xc and y > yc and (event.x, event.y) == (x, y):
                return 'S'
            # W
            elif x < xc and y == yc and (event.x, event.y) == (x, y):
                return 'W'
            # NE/NNE/ENE
            elif x > xc and y < yc and (event.x, event.y) == (x, y):
                if x + y == s:
                    return 'NE'
                elif x + y <= s - 2:
                    return 'NNE'
                elif x + y > s - 2 and x + y <= (s + s) / 100 * 75:
                    return 'ENE'
            # SE/ESE/SSE
            elif x > xc and y > yc and (event.x, event.y) == (x, y):
                if x == y:
                    return 'SE'
                elif x + y <= (s + s)- 2:
                    if x > y:
                        return 'ESE'
                    elif x < y:
                        return 'SSE'
            # SW/SSW/yc
            elif x < xc and y > yc and (event.x, event.y) == (x, y):
                if x + y == s:
                    return 'SW'
                elif x + y > s and x + y <= (s + s) / 100 * 75:
                    return 'SSW'
                elif x + y <= s - 2:
                    return 'WSW'
            # NW/WNW/NNW
            elif x < xc and y < yc and (event.x, event.y) == (x, y):
                if x == y:
                    return 'NW'
                elif x + y <= s - 2:
                    if x < y:
                        return 'WNW'
                    elif x > y:
                        return 'NNW'


ball = c.create_oval(200, 200, 300, 300, fill='green')

# None if tuple mode not active or int
v = 0
# geo direction (str)
direction = None
# False if direction is wrong or True if direction is correct
start_mv = False
# True or False in dependence ball currently moves or not
moving = False

def motion(event):
    global direction
    global ball
    global moving

    def start(event, direction, value=None, xm=None, ym=None):
        global ball
        global start_mv
        global moving

        if moving == False:
            if xm == None and ym == None:
                if start_mv == False:
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
                               lambda e=event, d=direction, x=xm, y=ym: start(e, d, xm=x, ym=y))
                    moving = True
        elif moving and xm != None and ym != None:
            int_mode = 0
            tuple_mode = 0
            if c.coords(ball)[0] == 0 or c.coords(ball)[1] == 0\
                    or c.coords(ball)[2] == 500 or c.coords(ball)[3] == 500:
                # W border
                if c.coords(ball)[0] == 0:
                    c.move(ball, 1, 0)
                # N border
                if c.coords(ball)[1] == 0:
                    c.move(ball, 0, 1)
                # E border
                if c.coords(ball)[2] == 500:
                    c.move(ball, -1, 0)
                # S border
                if c.coords(ball)[3] == 500:
                    c.move(ball, 0, -1)
                c.update()
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
                           lambda e=event, d=direction, v=None, x=xm, y=ym: start(e, d, v, xm=x, ym=y))
            # ----- Tuple mode -----
            # Round 1: xm = xm[0]; ym = ym[0] (repeat 2 times)
            # Round 2: xm = xm[1]; ym = ym[1] (repeat 1 time)
            # l = 0 -- Round 1
            # l = 1 -- Round 1
            # l = 2 -- Round 2; l = 0
            elif tuple_mode:
                if type(value) != int:
                    value = 0
                if value == 0:
                    c.move(ball, xm[0], ym[0])
                    c.update()
                    v = 1
                    root.after(10,
                               lambda e=event, d=direction, val=v, x=xm, y=ym: start(e, d, val, x, y))
                elif value == 1:
                    c.move(ball, xm[0], ym[0])
                    c.update()
                    v = 2
                    root.after(10,
                               lambda e=event, d=direction, val=v, x=xm, y=ym: start(e, d, val, x, y))
                elif value == 2:
                    c.move(ball, xm[1], ym[1])
                    c.update()
                    v = 0
                    root.after(10,
                               lambda e=event, d=direction, val=v, x=xm, y=ym: start(e, d, val, x, y))
            else:
                start_mv = False
                moving = False
    
    if moving == False:
        xc = int(c.coords(ball)[2] - ((c.coords(ball)[2] - c.coords(ball)[0]) / 2))
        yc = int(c.coords(ball)[3] - ((c.coords(ball)[3] - c.coords(ball)[1]) / 2))
        get_direction = getClickDirection(event, (xc, yc))
        print(get_direction)
        start(event, get_direction)


c.bind('<Button-1>', motion)


root.mainloop()
