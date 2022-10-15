from pico2d import *

running = True
image = None
logo_time = 0.0

def enter():
    global image
    pass

def exit():
    global image
    del image
    pass

def update():
    global logo_time
    global running
    if logo_time > 0.5:
        running = False
    delay(0.01)
    logo_time += 0.01
    pass

def draw():
    clear_canvas()

    update_canvas()
    pass

def handle_events():
    events = get_events()
    pass
