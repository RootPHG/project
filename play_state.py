from pico2d import *
import game_framework

import title_state
import logo_state

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

        # (캐릭터가 바라보는 방향)



class Monster:
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


def handle_events():
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        #     KEY DOWN
        elif (event.type, event.key) == (SDL_KEYDOWN< SDLK_ESCAPE):
            # game_framework.change_state(logo_state)
            game_framework.quit()
        else:
            ranger.handle_event(event)




ranger = None
running = None


def enter():
    global ranger, running
    ranger = Ranger()
    running = True

def exit():
    global ranger
    del ranger

def update():
    ranger.update()

def draw():
    clear_canvas()
    ranger.draw()
    update_canvas()


# open_canvas()
#
# enter()
# while running:
#     handle_events()
#     update()
#     draw()
#
# exit()
#
# close_canvas()


