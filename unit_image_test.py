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
            elif event.key == SDLK_LEFT:
                dir_x -= 1
            elif event.key == SDLK_UP:
                dir_y += 1
            elif event.key == SDLK_DOWN:
                dir_y -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir_x -= 1
            elif event.key == SDLK_LEFT:
                dir_x += 1
            elif event.key == SDLK_UP:
                dir_y -= 1
            elif event.key == SDLK_DOWN:
                dir_y += 1

def head_dir():
    global dir_x
    global dir_y
    global anime

    # (캐릭터가 바라보는 방향)
    if dir_x < 0 and dir_y < 0:
        anime = 0
    elif dir_x < 0 and dir_y == 0:
        anime = 1
    elif dir_x < 0 and dir_y > 0:
        anime = 2
    elif dir_x == 0 and dir_y > 0:
        anime = 3
    elif dir_x > 0 and dir_y > 0:
        anime = 4
    elif dir_x > 0 and dir_y == 0:
        anime = 5
    elif dir_x > 0 and dir_y < 0:
        anime = 6
    elif dir_x == 0 and dir_y < 0:
        anime = 7

open_canvas()

main_char2 = load_image('ranger_sprite.png')

running = True
frame = 0
dir_x = 0
dir_y = 0
x = 800 // 2
y = 600 // 2
anime = 0

while running:
    clear_canvas()
    main_char2.clip_draw(frame * 62 + 200, anime * 79 + 15, 60, 84, x, y)
    update_canvas()
    # 멈췄을경우 이미지 고정
    if dir_x == 0 and dir_y == 0:
        frame = 3
    else :
        frame = (frame + 1) % 8
    delay(0.05)
    head_dir()
    x += dir_x * 5
    y += dir_y * 5
    handle_events()

close_canvas()


