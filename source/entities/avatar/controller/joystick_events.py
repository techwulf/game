from source.interface import joystick

class JoystickEvents:
    def __init__(self):
        joystick.AXIS_0.subscribe(self)
        joystick.AXIS_1.subscribe(self)
        joystick.AXIS_2.subscribe(self)
        joystick.AXIS_3.subscribe(self)
        joystick.BUTTON_0.subscribe(self)
        joystick.BUTTON_1.subscribe(self)
        joystick.BUTTON_2.subscribe(self)
        joystick.BUTTON_3.subscribe(self)
        joystick.BUTTON_4.subscribe(self)
        joystick.BUTTON_5.subscribe(self)
        joystick.BUTTON_6.subscribe(self)
        joystick.BUTTON_7.subscribe(self)
        joystick.BUTTON_8.subscribe(self)
        joystick.BUTTON_9.subscribe(self)
        joystick.BUTTON_10.subscribe(self)
        joystick.BUTTON_11.subscribe(self)

        joystick.HAT_UP.subscribe(self)
        joystick.HAT_DOWN.subscribe(self)
        joystick.HAT_LEFT.subscribe(self)
        joystick.HAT_RIGHT.subscribe(self)
        pass

    def on_axis_0(self, value):
        self.move_x(value)
        pass

    def on_axis_1(self, value):
        self.move_y(value)
        pass

    def on_axis_2(self, value):
        self.move_x(value)
        pass

    def on_axis_3(self, value):
        self.move_y(value)
        pass

    def on_button_1_down(self):
        self.run()
        pass

    def on_button_1_up(self):
        self.walk()
        pass

    def on_button_0_up(self):
        pass
    def on_button_0_down(self):
        pass
    def on_button_2_up(self):
        pass
    def on_button_2_down(self):
        pass
    def on_button_3_up(self):
        pass
    def on_button_3_down(self):
        pass
    def on_button_4_up(self):
        pass
    def on_button_4_down(self):
        pass
    def on_button_5_up(self):
        pass
    def on_button_5_down(self):
        pass
    def on_button_6_up(self):
        pass
    def on_button_6_down(self):
        pass
    def on_button_7_up(self):
        pass
    def on_button_7_down(self):
        pass
    def on_button_8_up(self):
        pass
    def on_button_8_down(self):
        pass
    def on_button_9_up(self):
        pass
    def on_button_9_down(self):
        pass
    def on_button_10_up(self):
        pass
    def on_button_10_down(self):
        pass
    def on_button_11_up(self):
        pass
    def on_button_11_down(self):
        pass

    def on_hatup_up(self):
        pass
    def on_hatdown_up(self):
        pass
    def on_hatup_down(self):
        pass
    def on_hatdown_down(self):
        pass
    def on_hatup_left(self):
        pass
    def on_hatdown_left(self):
        pass
    def on_hatup_right(self):
        pass
    def on_hatdown_right(self):
        pass

