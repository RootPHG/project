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

class RUN_STAND:
    def enter(self, event):
        print('ENTER IDLE')
        self.frame = 3
        pass

    def exit(self):
        print('ENTER IDLE')
        pass

    def do(self):

        pass

    def draw(self):
        self.move_image.clip_draw(self.frame * 62 + 200, self.anime * 79 + 15, 60, 84, self.x, self.y)


class ATTACK:
    def enter(self, event):
        print('ENTER RUN_X')
        pass

    def exit(self):
        print('EXIT RUN_X')
        pass

    def do(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir_x * 5
        self.y += self.dir_y * 5
        pass

    def draw(self):
        self.move_image.clip_draw(self.frame * 62 + 200, self.anime * 79 + 15, 60, 84, self.x, self.y)




next_state = {
    RUN_STAND: {RD: RUN_STAND, LD: RUN_STAND, UD: RUN_STAND, DD: RUN_STAND, RU: RUN_STAND, LU: RUN_STAND, UU: RUN_STAND, DU: RUN_STAND,SPACE: ATTACK},
    ATTACK: {TIMER: RUN_STAND},
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

        self.event_que = []
        self.cur_state = RUN_STAND
        self.cur_state.enter()

    def update(self):
        if self.attack == 0:
            self.cur_state.do(self)

            if self.event_que:
                event = self.event_que.pop()
                self.cur_state.exit(self)
                self.cur_state = next_state[self.cur_state][event]
                self.cur_state.enter(self, event)

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

            delay(0.04)

        elif self.attack == 1:
            self.frame = (self.frame + 1) % 4

            if self.frame == 0:
                self.attack = 0
            delay(0.1)

        pass

    def draw(self):
        if self.attack == 0:
            self.cur_state.draw(self)
            # self.move_image.clip_draw(self.frame * 62 + 200, self.anime * 79 + 15, 60, 84, self.x, self.y)
        elif self.attack == 1:
            self.att_image.clip_draw(self.frame * 78 + 135, self.anime * 91 + 25, 60, 84, self.x - 5, self.y)

    def add_event(self, event):
        self.event_que.insert(0, event)


def handle_event(self, event):
    if (event.type, event.key) in key_event_table:
        key_event = key_event_table[(event.type, event.key)]
        self.add_event(key_event)


