def setup():
    size(640, 480)

xx = 40
yy = 240
x_speed = 3
y_speed = 2

def draw_ship(x, y):
    ellipse(x, y, 40, 20)
    triangle(x, y+20, x, y-20, x+80, y) 

def draw():
    global xx, yy, x_speed, y_speed
    background(200)
    draw_ship(xx, yy)
    xx = (xx + x_speed + width) % width
    if keyPressed:
        if key == 'a':
            x_speed = -1 * abs(x_speed)
        if key == 'd':
            x_speed = abs(x_speed)
        if key == 'w':
            yy = yy - y_speed
        if key == 's':
            yy = yy + y_speed
