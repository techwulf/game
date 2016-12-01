from pygame.locals import *

class Keyboard:
    ESCAPE = False
    L_SHIFT = False
    R_SHIFT = False
    UP = False
    DOWN = False
    LEFT = False
    RIGHT = False

    def key_event(self, event):
        if event.type == KEYDOWN:
            self.on_key_down(event.key)
        elif event.type == KEYUP:
            self.on_key_up(event.key)

    def on_key_down(self, key):
        if key == K_ESCAPE:
            self.ESCAPE = True
        elif key == K_LSHIFT:
            self.L_SHIFT = True
        elif key == K_UP:
            self.UP = True
        elif key == K_DOWN:
            self.DOWN = True
        elif key == K_LEFT:
            self.LEFT = True
        elif key == K_RIGHT:
            self.RIGHT = True
    
    def on_key_up(self, key):
        if key == K_ESCAPE:
            self.L_ESCAPE = False
        elif key == K_LSHIFT:
            self.L_SHIFT = False
        elif key == K_UP:
            self.UP = False
        elif key == K_DOWN:
            self.DOWN = False
        elif key == K_LEFT:
            self.LEFT = False
        elif key == K_RIGHT:
            self.RIGHT = False

KEYBOARD = Keyboard()