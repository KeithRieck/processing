def setup():
    size(640, 480)

xx = 40
yy = 240
speed = 3

def draw_shape(x, y):
    ellipse(x, y, 40, 20)
    triangle(x, y+20, x, y-20, x+80, y) 

def draw():
    global xx, yy, speed
    background(200)
    draw_shape(xx, yy)
    xx = xx + speed
    if xx > 640:
        xx = 0
    elif xx < 0:
        xx = 640
    if keyPressed:
        speed = speed * -1
