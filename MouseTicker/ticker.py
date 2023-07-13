import time
import pyautogui
import random


def random_mouse_movement(duration):
    print("CTRL + D to stop")
    while True:

        direction = random.choice(['up', 'down', 'right', 'left'])
        current_x, current_y = pyautogui.position()

        if direction == 'up':
            new_x = current_x
            new_y = current_y - 100
        elif direction == 'down':
            new_x = current_x
            new_y = current_y + 100
        elif direction == 'left':
            new_x = current_x - 100
            new_y = current_y
        elif direction == 'right':
            new_x = current_x + 100
            new_y = current_y
        else:
            raise Exception("Not horizontal or vertical move!!!")

        pyautogui.moveTo(new_x, new_y)
        time.sleep(duration)


random_mouse_movement(2)