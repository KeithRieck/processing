def random_angle():
    speed = 2
    angle = (random(1000)/1000.0) * 6.283
    dx = speed * cos(angle)
    dy = speed * sin(angle)
    return (angle, dx, dy)

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
    image(img, x, y)
    x = x + dx
    y = y + dy
    if (x + img.width) > width or x < 0:
        dx = dx * -1
    if (y + img.height) > height or y < 0:
        dy = dy * -1
