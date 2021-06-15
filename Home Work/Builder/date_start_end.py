class Period:
    def __init__(self, start, end):
        if start < end:
            self.start = start
            self.end = end
        else:
            raise ValueError('start date must be lesser when end date')

    def __str__(self):
        return f"Start date: {self.start}; End date: {self.end}"     # e.g. "[01.01.2021 .. 02.01.2021]"
