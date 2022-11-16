from pico2d import *

RD, LD, UD, DD, RU, LU, UU, DU, SPACE, TIMER= range(10)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RD,
    (SDL_KEYDOWN, SDLK_LEFT): LD,
    (SDL_KEYDOWN, SDLK_UP): UD,
    (SDL_KEYDOWN, SDLK_DOWN): DD,
    (SDL_KEYUP, SDLK_RIGHT): RU,
    (SDL_KEYUP, SDLK_LEFT): LU,
    (SDL_KEYUP, SDLK_UP): UU,
    (SDL_KEYUP, SDLK_DOWN): DU,
    (SDL_KEYDOWN, SDLK_SPACE): SPACE
}

class IDLE:
    def enter():
        pass

    def exit():
        pass

    def do():
        pass

    def draw():
        pass


class RUN_X:
    def enter():
        pass

    def exit():
        pass

    def do():
        pass

    def draw():
        pass

class RUN_Y:
    def enter():
        pass

    def exit():
        pass

    def do():
        pass

    def draw():
        pass

class RUN_Z:
    def enter():
        pass

    def exit():
        pass

    def do():
        pass

    def draw():
        pass

class SHOT:
    def enter():
        pass

    def exit():
        pass

    def do():
        pass

    def draw():
        pass

next_state = {
    IDLE: {},
    RUN_X: {},
    RUN_Y: {},
    RUN_Z: {},
    SHOT: {}
}


class Ranger:
    move_image = None
    att_image = None

    def __init__(self):
        self.x, self.y = 800 // 2, 600 // 2
        self.dir_x = 0
        self.dir_y = 0
        self.frame = 0
        self.anime = 0
        self.attack = 0
        if Ranger.move_image == None:
            self.move_image = load_image('ranger_sprite.png')
        if Ranger.att_image == None:
            self.att_image = load_image('ranger_attack.png')

    def update(self):
        if self.attack == 0:
            if self.dir_x < 0 and self.dir_y < 0:
                self.anime = 0
            elif self.dir_x < 0 and self.dir_y == 0:
                self.anime = 1
            elif self.dir_x < 0 and self.dir_y > 0:
                self.anime = 2
            elif self.dir_x == 0 and self.dir_y > 0:
                self.anime = 3
            elif self.dir_x > 0 and self.dir_y > 0:
                self.anime = 4
            elif self.dir_x > 0 and self.dir_y == 0:
                self.anime = 5
            elif self.dir_x > 0 and self.dir_y < 0:
                self.anime = 6
            elif self.dir_x == 0 and self.dir_y < 0:
                self.anime = 7

            if self.dir_x == 0 and self.dir_y == 0:
                self.frame = 3
            else:
                self.frame = (self.frame + 1) % 8
            self.x += self.dir_x * 5
            self.y += self.dir_y * 5

            delay(0.04)
        elif self.attack == 1:
            self.frame = (self.frame + 1) % 4

            if self.frame == 0:
                self.attack = 0
            delay(0.1)

        pass

    def draw(self):
        if self.attack == 0:
            self.move_image.clip_draw(self.frame * 62 + 200, self.anime * 79 + 15, 60, 84, self.x, self.y)
        elif self.attack == 1:
            self.att_image.clip_draw(self.frame * 78 + 135, self.anime * 91 + 25, 60, 84, self.x - 5, self.y)

        pass