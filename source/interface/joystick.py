import pygame

class Joystick:
    joystick    = None
    name        = None

    dead_zone   = 0.20

    AXIS_0      = 0
    AXIS_1      = 0
    AXIS_2      = 0
    AXIS_3      = 0
    BUTTON_0    = None
    BUTTON_1    = None
    BUTTON_2    = None
    BUTTON_3    = None
    BUTTON_4    = None
    BUTTON_5    = None
    BUTTON_6    = None
    BUTTON_7    = None
    BUTTON_8    = None
    BUTTON_9    = None
    BUTTON_10   = None
    BUTTON_11   = None

    def __init__(self):
        pygame.joystick.init()
        joystick_count = pygame.joystick.get_count()
        for i in range(joystick_count):
            self.joystick = pygame.joystick.Joystick(i)
            self.joystick.init()
            self.name = self.joystick.get_name()
        print(self.name)

    def joystick_event(self, event):
        if event.type == pygame.JOYBUTTONDOWN:
            self.on_button_down()
        if event.type == pygame.JOYBUTTONUP:
            self.on_button_up()
        if event.type == pygame.JOYAXISMOTION:
            self.on_axis_motion()
        #if event.type == pygame.JOYBALLMOTION:
            #print("Joystick Ball Motion.")
        if event.type == pygame.JOYHATMOTION:
            self.on_hat_motion()
        pass

    def on_axis_motion(self):
        axes = self.joystick.get_numaxes()
        for axis in range(axes):
            if axis == 0:
                value = self.joystick.get_axis(axis)
                if value > self.dead_zone or value < -self.dead_zone:
                    self.AXIS_0 = value
                else:
                    self.AXIS_0 = 0
            if axis == 1:
                value = self.joystick.get_axis(axis)
                if value > self.dead_zone or value < -self.dead_zone:
                    self.AXIS_1 = value
                else:
                    self.AXIS_1 = 0
            if axis == 2:
                value = self.joystick.get_axis(axis)
                if value > self.dead_zone or value < -self.dead_zone:
                    self.AXIS_2 = value
                else:
                    self.AXIS_2 = 0
            if axis == 3:
                value = self.joystick.get_axis(axis)
                if value > self.dead_zone or value < -self.dead_zone:
                    self.AXIS_3 = value
                else:
                    self.AXIS_3 = 0

    def get_axis_value(self, axis, AXIS):
        value = self.joystick.get_axis(axis)
        if value > self.dead_zone or value < -self.dead_zone:
            AXIS = value
        else:
            AXIS = 0
        pass

    def on_hat_motion(self):
        hats = self.joystick.get_numhats()
        for hat in range(hats):
            direction = self.joystick.get_hat(hat)
            if direction[0] == -1:
                pass
            if direction[0] == 1:
                pass
            if direction[1] == 1:
                pass
            if direction[1] == -1:
                pass
        pass


    def on_button_down(self):
        buttons = self.joystick.get_numbuttons()
        for button in range(buttons):
            if button == 0 and self.joystick.get_button(button):
                self.BUTTON_0 = True
            if button == 1 and self.joystick.get_button(button):
                self.BUTTON_1 = True
            if button == 2 and self.joystick.get_button(button):
                self.BUTTON_2 = True
            if button == 3 and self.joystick.get_button(button):
                self.BUTTON_3 = True
            if button == 4 and self.joystick.get_button(button):
                self.BUTTON_4 = True
            if button == 5 and self.joystick.get_button(button):
                self.BUTTON_5 = True
            if button == 6 and self.joystick.get_button(button):
                self.BUTTON_6 = True
            if button == 7 and self.joystick.get_button(button):
                self.BUTTON_7 = True
            if button == 8 and self.joystick.get_button(button):
                self.BUTTON_8 = True
            if button == 9 and self.joystick.get_button(button):
                self.BUTTON_9 = True
            if button == 10 and self.joystick.get_button(button):
                self.BUTTON_10 = True
            if button == 11 and self.joystick.get_button(button):
                self.BUTTON_11 = True

    def on_button_up(self):
        buttons = self.joystick.get_numbuttons()
        for button in range(buttons):
            if button == 0 and self.joystick.get_button(button) == 0:
                self.BUTTON_0 = False
            if button == 1 and self.joystick.get_button(button) == 0:
                self.BUTTON_1 = False
            if button == 2 and self.joystick.get_button(button) == 0:
                self.BUTTON_2 = False
            if button == 3 and self.joystick.get_button(button) == 0:
                self.BUTTON_3 = False
            if button == 4 and self.joystick.get_button(button) == 0:
                self.BUTTON_4 = False
            if button == 5 and self.joystick.get_button(button) == 0:
                self.BUTTON_5 = False
            if button == 6 and self.joystick.get_button(button) == 0:
                self.BUTTON_6 = False
            if button == 7 and self.joystick.get_button(button) == 0:
                self.BUTTON_7 = False
            if button == 8 and self.joystick.get_button(button) == 0:
                self.BUTTON_8 = False
            if button == 9 and self.joystick.get_button(button) == 0:
                self.BUTTON_9 = False
            if button == 10 and self.joystick.get_button(button) == 0:
                self.BUTTON_10 = False
            if button == 11 and self.joystick.get_button(button) == 0:
                self.BUTTON_11 = False

JOYSTICK = Joystick()
