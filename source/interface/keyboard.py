from pygame.locals import *

class Keyboard:
    def key_event(self, event):
        if event.type == KEYDOWN:
            self.on_key_down(event.key)
        if event.type == KEYUP:
            self.on_key_up(event.key)

    def on_key_down(self, key):
        if key == K_a:
            KEY_A.down()
        elif key == K_m:
            KEY_M.down()
        elif key == K_UP:
            KEY_UP.down()
        elif key == K_DOWN:
            KEY_DOWN.down()
        elif key == K_LEFT:
            KEY_LEFT.down()
        elif key == K_RIGHT:
            KEY_RIGHT.down()
        elif key == K_ESCAPE:
            KEY_ESCAPE.down()
        elif key == K_LSHIFT:
            KEY_L_SHIFT.down()
        elif key == K_RETURN:
            KEY_RETURN.down()

    def on_key_up(self, key):
        if key == K_a:
            KEY_A.up()
        elif key == K_m:
            KEY_M.up()
        elif key == K_UP:
            KEY_UP.up()
        elif key == K_DOWN:
            KEY_DOWN.up()
        elif key == K_LEFT:
            KEY_LEFT.up()
        elif key == K_RIGHT:
            KEY_RIGHT.up()
        elif key == K_ESCAPE:
            KEY_ESCAPE.up()
        elif key == K_LSHIFT:
            KEY_L_SHIFT.up()
        elif key == K_RETURN:
            KEY_RETURN.up()

class KeyA:
    subscribers = []
    value = False
    
    def __init__(self):
        pass
    
    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)
        pass
    
    def down(self):
        self.value = True
        for subscriber in self.subscribers:
            subscriber.on_keydown_a()
        pass

    def up(self):
        self.value = False
        for subscriber in self.subscribers:
            subscriber.on_keyup_a()
        pass

class KeyM:
    subscribers = []
    value = False
    
    def __init__(self):
        pass
    
    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)
        pass
    
    def down(self):
        self.value = True
        for subscriber in self.subscribers:
            subscriber.on_keydown_m()
        pass

    def up(self):
        self.value = False
        for subscriber in self.subscribers:
            subscriber.on_keyup_m()
        pass

class KeyUp:
    subscribers = []
    value = False
    
    def __init__(self):
        pass
    
    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)
        pass
    
    def down(self):
        self.value = True
        for subscriber in self.subscribers:
            subscriber.on_keydown_up()
        pass

    def up(self):
        self.value = False
        for subscriber in self.subscribers:
            subscriber.on_keyup_up()
        pass

class KeyDown:
    subscribers = []
    value = False

    def __init__(self):
        pass

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)
        pass

    def down(self):
        self.value = True
        for subscriber in self.subscribers:
            subscriber.on_keydown_down()
        pass

    def up(self):
        self.value = False
        for subscriber in self.subscribers:
            subscriber.on_keyup_down()
        pass

class KeyLeft:
    subscribers = []
    value = False
    
    def __init__(self):
        pass

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)
        pass

    def down(self):
        self.value = True
        for subscriber in self.subscribers:
            subscriber.on_keydown_left()
        pass

    def up(self):
        self.value = False
        for subscriber in self.subscribers:
            subscriber.on_keyup_left()
        pass

class KeyRight:
    subscribers = []
    value = False
    
    def __init__(self):
        pass

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)
        pass

    def down(self):
        self.value = True
        for subscriber in self.subscribers:
            subscriber.on_keydown_right()
        pass

    def up(self):
        self.value = False
        for subscriber in self.subscribers:
            subscriber.on_keyup_right()
        pass

class KeyEscape:
    subscribers = []
    value = False

    def __init__(self):
        pass

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)
        pass

    def down(self):
        self.value = True
        for subscriber in self.subscribers:
            subscriber.on_keydown_escape()
        pass

    def up(self):
        self.value = False
        for subscriber in self.subscribers:
            subscriber.on_keyup_escape()

class KeyReturn:
    subscribers = []
    value = False
    
    def __init__(self):
        pass

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)
        pass

    def down(self):
        self.value = True
        for subscriber in self.subscribers:
            subscriber.on_keydown_return()
        pass

    def up(self):
        self.value = False
        for subscriber in self.subscribers:
            subscriber.on_keyup_return()

class KeyLShift:
    subscribers = []
    value = False
    
    def __init__(self):
        pass

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)
        pass

    def down(self):
        self.value = True
        for subscriber in self.subscribers:
            subscriber.on_keydown_left_shift()
        pass

    def up(self):
        self.value = False
        for subscriber in self.subscribers:
            subscriber.on_keyup_left_shift()

KEYBOARD    = Keyboard()
KEY_A       = KeyA()
KEY_M       = KeyM()
KEY_UP      = KeyUp()
KEY_DOWN    = KeyDown()
KEY_LEFT    = KeyLeft()
KEY_RIGHT   = KeyRight()
KEY_RETURN  = KeyReturn()
KEY_ESCAPE  = KeyEscape()
KEY_L_SHIFT = KeyLShift()
