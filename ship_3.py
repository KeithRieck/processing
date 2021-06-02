
x_ship = 40
y_ship = 240
x_speed = 3
y_speed = 2
x_rock = 320
y_rock = 240
dx_rock = 1
dy_rock = 1
score = 0
lives = 3

def random_angle():
    speed = 3
    angle = (random(1000)/1000.0) * 3.14159 * 2
    dx =  speed * cos(angle)
    dy =  speed * sin(angle)
    return dx, dy

def is_touching(x1, y1, w1, h1,   x2, y2, w2, h2):
    if y1+h1 < y2:
        return False
    elif y1 > y2+h2:
        return False
    if x1+w1 < x2:
        return False
    elif x1 > x2+w2:
        return False
    return True

def draw_ship(x, y):
    fill('#C11232')
    ellipse(x, y, 60, 15)
    fill('#FAF208')
    triangle(x, y+20, x, y-20, x+80, y) 
    fill('#000000')
    
def draw_rock(x, y):
    fill('#CCCCCC')
    ellipse(x+30, y+30, 60, 60)
    
def reset_rock():
    x = random(width - 40) + 20
    y = random(height - 40) + 20
    dx, dy = random_angle()
    return x, y, dx, dy

def setup():
    global dx_rock, dy_rock
    size(640, 480)
    reset_rock()
    dx_rock, dy_rock = random_angle()
    font = createFont("monospace", 24)
    textFont(font)

def draw():
    global score, lives, x_ship, y_ship, x_speed, y_speed, x_rock, y_rock, dx_rock, dy_rock
    background(64)
    text(str(score), 30, 30)
    text("Lives: " + str(lives), (width - 100), 30)
    if lives <= 0:
        text("GAME OVER", width/2 - 80, height/2)
        return
    x_rock = x_rock + dx_rock
    y_rock = y_rock + dy_rock
    if x_rock + 60 > width or x_rock < 0:
        dx_rock = -1 * dx_rock
    if y_rock + 60 > height or y_rock < 0:
        dy_rock = -1 * dy_rock
    x_ship = x_ship + x_speed
    if x_ship > width:
        x_ship = 0
        score = score + 1
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
    draw_rock(x_rock, y_rock)
    if is_touching(x_ship-30, y_ship-20, 80, 40,  x_rock, y_rock, 60, 60):
        x_rock, y_rock, dx_rock, dy_rock = reset_rock()
        lives = lives - 1

