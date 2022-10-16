import pico2d
import game_framework

import logo_state
import play_state

state = [logo_state, play_state]

pico2d.open_canvas()

state.enter()

while state.running:
    state.handle_events()
    state.update()
    state.draw()

state.exit()

pico2d.close_canvas()