from source.abstract.entities.human import controller
import keyboard_events
import joystick_events

class Controller(controller.Controller, keyboard_events.KeyboardEvents, joystick_events.JoystickEvents):
    def __init__(self):
        controller.Controller.__init__(self)
        keyboard_events.KeyboardEvents.__init__(self)
        joystick_events.JoystickEvents.__init__(self)
        pass

    def on_loop(self):
        self.translate()
        self.set_animation()
        self.set_direction()
        pass
