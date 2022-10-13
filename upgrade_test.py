from pico2d import *

class Ranger:
    global dir_x, dir_y
    global anime
    def __init__(self):
        self.x, self.y = 800 // 2, 600 // 2
        self.frame = 0
        self.move_image = load_image('ranger_sprite.png')
        self.att_image = load_image('ranger_attack.png')
    def update(self):
        if dir_x == 0 and dir_y == 0:
            self.frame = 3
        else:
            self.frame = (self.frame + 1) % 8
        self.x += dir_x * 5
        self.y += dir_y * 5
        head_dir()
        pass
    def draw(self):
        self.move_image.clip_draw(self.frame * 62 + 200, anime * 79 + 15, 60, 84, self.x, self.y)
        pass


class Monster:
    def __init__(self):
        pass
    def update(self):

        pass
    def draw(self):
        pass


def handle_events():
    global running
    global dir_x
    global dir_y
    global anime

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        #     KEY DOWN
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir_x += 1
            elif event.key == SDLK_LEFT:
                dir_x -= 1
            elif event.key == SDLK_UP:
                dir_y += 1
            elif event.key == SDLK_DOWN:
                dir_y -= 1
            elif event.key == SDLK_SPACE:
                
            elif event.key == SDLK_ESCAPE:
                running = False
        #         KEY UP
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




# initialization code
open_canvas()
dir_x, dir_y = 0, 0
anime = 0
ranger = Ranger()
running = True

# game main loop code
while running:
    handle_events()

    ranger.update()

    clear_canvas()
    ranger.draw()
    update_canvas()

    delay(0.04)

# finalization code
close_canvas()
