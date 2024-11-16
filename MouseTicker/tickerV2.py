# TODO: to fix, 'e' doesn't work


# import time
# import pyautogui
# import random
# import threading
# import msvcrt
#
# def random_mouse_movement(duration):
#     while True:
#
#         direction = random.choice(['up', 'down', 'right', 'left'])
#         current_x, current_y = pyautogui.position()
#
#         if direction == 'up':
#             new_x = current_x
#             new_y = current_y - 100
#         elif direction == 'down':
#             new_x = current_x
#             new_y = current_y + 100
#         elif direction == 'left':
#             new_x = current_x - 100
#             new_y = current_y
#         elif direction == 'right':
#             new_x = current_x + 100
#             new_y = current_y
#         else:
#             raise Exception("Not horizontal or vertical move!!!")
#
#         pyautogui.moveTo(new_x, new_y)
#         time.sleep(duration)
#
# def input_scanner():
#     while True:
#         if msvcrt.kbhit():
#             key = msvcrt.getch().decode("utf-8").lower()
#             if key == 'e':
#                 print('e')
#                 print('Mouse ticker finished his job to tick the mouse :).')
#                 break
#             else:
#                 print('Only e works to stop the script!!!')
#         time.sleep(0.1)
#
# movement_thread = threading.Thread(target=random_mouse_movement, args=(2,))
# movement_thread.start()
#
# random_mouse_movement(2)