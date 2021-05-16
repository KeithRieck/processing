def random_angle():
    speed = 3
    angle = (random(1000)/1000.0) * 6.283
    dx = speed * cos(angle)
    dy = speed * sin(angle)
    return (angle, dx, dy)

def is_colliding(x1, y1, w1, h1, x2, y2, w2, h2):
    if y1+h1 < y2:
        return False
    elif y1 > y2+h2:
        return False
    if x1+w1 < x2:
        return False
    elif x1 > x2+w2:
        return False
    return True

def setup():
    global img, x, y, dx, dy
    size(640, 480)
    img = loadImage("https://raw.githubusercontent.com/KeithRieck/processing/main/duke.gif")
    x = width / 2
    y = height / 2
    (angle, dx, dy) = random_angle()
    
def draw():
    global img, x, y, dx, dy
    background(200)
    x = x + dx
    y = y + dy
    if (x + img.width) > width or x < 0:
        dx = dx * -1
    if (y + img.height) > height or y < 0:
        dy = dy * -1
    if is_colliding(x, y, img.width, img.height, 320, 240, 150, 150):
        fill("#FFFF00")
    rect(320, 240, 150, 150)
    fill("#FFFFFF")
    image(img, x, y)
