import pygame
import time
import vgamepad as vg

# initialization stuff
pygame.init()
pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)
gamepad = vg.VX360Gamepad()

# key binds for virtual joystick
up = vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB
down = vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB

# key bindings for g923
gears = {-1: 11,
          1: 12,
          2: 13,
          3: 14,
          4: 15,
          5: 16,
          6: 17
        }

# default values
gear = 0
prev_gear = gear

def shift(direction, hops):
    for x in range(hops):
        gamepad.press_button(button=direction)
        gamepad.update()
        time.sleep(0.2)
        gamepad.release_button(button=direction)
        gamepad.update()
        time.sleep(0.4)

while True:
    for event in pygame.event.get():
        if event.type == pygame.JOYBUTTONDOWN:
            for gear in gears:
                if joystick.get_button(gears[gear]) and joystick.get_axis(3) < 0.75:
                    print(f"gear {gear} was selected.")
                    print(f"previous gear was {prev_gear}")
                    if gear > prev_gear:
                        shift(up, (gear - prev_gear))
                    elif gear < prev_gear:
                        shift(down, (prev_gear - gear))
                    print(f"Gear {gear} engaged.")
                    prev_gear = gear
