from pico2d import *

def handle_events():
    global running
    global dir_x
    global dir_y
    global anime

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir_x += 1
                anime = 1
            elif event.key == SDLK_LEFT:
                dir_x -= 1
                anime = 0
            elif event.key == SDLK_UP:
                dir_y += 1
                anime -= 2
            elif event.key == SDLK_DOWN:
                dir_y -= 1
                anime -= 2
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir_x -= 1
                anime = 3
            elif event.key == SDLK_LEFT:
                dir_x += 1
                anime = 2
            elif event.key == SDLK_UP:
                dir_y -= 1
                anime += 2
            elif event.key == SDLK_DOWN:
                dir_y += 1
                anime += 2


open_canvas()

main_char1 = load_image('doom_character1.png')
main_char2 = load_image('doom_pistol.png')
main_char3 = load_image('character_type_swat.png')
main_char4 = load_image('main_character.png')
mod_char = load_image('clasic_monster.png')

running = True
frame = 0
dir_x = 0
dir_y = 0
anime = 0

while running:
    clear_canvas()
    # main_char1
    update_canvas()
    # frame = (frame + 1) %
    delay(0.05)
    x += dir_x * 5
    y += dir_y * 5
    handle_events()

close_canvas()
