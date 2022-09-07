def draw_line(length: int, direction: str):
    print({'h': '-', 'v': '|\n'}[direction] * length)


if __name__ == '__main__':
    draw_line(5, 'h')
    draw_line(3, 'v')
