from source.interface import keyboard

class KeyboardEvents:
    def __init__(self):
        keyboard.KEY_A.subscribe(self)
        keyboard.KEY_M.subscribe(self)
        keyboard.KEY_UP.subscribe(self)
        keyboard.KEY_DOWN.subscribe(self)
        keyboard.KEY_RIGHT.subscribe(self)
        keyboard.KEY_LEFT.subscribe(self)
        keyboard.KEY_RETURN.subscribe(self)
        keyboard.KEY_L_SHIFT.subscribe(self)
        pass

    def on_keydown_a(self):
        pass

    def on_keyup_a(self):
        pass

    def on_keydown_m(self):
        self.mine()
        pass

    def on_keyup_m(self):
        pass

    def on_keydown_up(self):
        self.move_y(-1)
        pass

    def on_keyup_up(self):
        self.move_y(0)
        pass

    def on_keydown_right(self):
        self.move_x(1)
        pass

    def on_keyup_right(self):
        self.move_x(0)
        pass

    def on_keydown_down(self):
        self.move_y(1)
        pass

    def on_keyup_down(self):
        self.move_y(0)
        pass

    def on_keydown_left(self):
        self.move_x(-1)
        pass

    def on_keyup_left(self):
        self.move_x(0)
        pass

    def on_keydown_left_shift(self):
        self.run()
        pass

    def on_keyup_left_shift(self):
        self.walk()
        pass

    def on_keydown_return(self):
        self.pickup()
        pass

    def on_keyup_return(self):
        pass
