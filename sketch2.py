
x_ship = 40
y_ship = 240
x_speed = 3
y_speed = 2
x_target = 320
y_target = 240

def draw_ship(x, y):
    ellipse(x, y, 40, 20)
    triangle(x, y+20, x, y-20, x+80, y) 

def draw_target(x, y):
    rect(x, y, 40, 40)

def reset_target():
    global x_target, y_target
    x_target = random(width - 40) + 20
    y_target = random(height - 40) + 20

def hit_target(x, y):
    global x_target, y_target
    return y>y_target and y<y_target+40 and x>x_target-60 and x<x_target+20

def setup():
    size(640, 480)
    reset_target()

def draw():
    global x_ship, y_ship, x_speed, y_speed, x_target, y_target
    background(200)
    x_ship = x_ship + x_speed
    if x_ship > width:
        x_ship = 0
    elif x_ship < 0:
        x_ship = width
    if keyPressed:
        if key == 'a':
            x_speed = -1 * abs(x_speed)
        if key == 'd':
            x_speed = abs(x_speed)
        if key == 'w' and x_speed > 0:
            y_ship = y_ship - y_speed
        if key == 's' and x_speed > 0:
            y_ship = y_ship + y_speed
    draw_ship(x_ship, y_ship)
    draw_target(x_target, y_target)
    if hit_target(x_ship, y_ship):
        reset_target()
