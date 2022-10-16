import game_framework
from pico2d import *

import play_state

image = None
logo_time = 0.0

def enter():
    global image
    image = load_image('TUK_logo.jpg')
    pass

def exit():
    global image
    del image
    pass

def update():
    global logo_time
    if logo_time > 0.5:
        logo_time = 0
        game_framework.change_state(play_state)
    delay(0.01)
    logo_time += 0.01
    pass

def draw():
    clear_canvas()
    image.draw(400,300)
    update_canvas()
    pass

def handle_events():
    events = get_events()
    pass


