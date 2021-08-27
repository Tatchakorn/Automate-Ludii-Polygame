"""
Author: Saitako
GUI automation for Ludii and Polygame

P.S. Too lazy to implement this using subprocess
""" 

import time
import re
from pathlib import Path

import pyautogui
import pyperclip

pyautogui.PAUSE = 0.3

# UI Positions (x, y)
LUDII_UI_POS = (1647, 15)
TERMINAL_UI_POS = (636, 370)
MBXTERM_UI_POS = (500, 23)

# MobaXterm log file
MOBAX_LOG_PATH = r'fake.log'

# ludii output text
MOVE_TEXT_LENGTH = 230
BEGIN_LINE_POS = (1600, 493)
old_result = ''

# ---- IMPORTANT ----
START_AUTO_AT_MV = 10
current_mv = 0


def goto_(app: str):
    if app == 'ludii':
        pyautogui.click(*LUDII_UI_POS)
    elif app == 'terminal':
        pyautogui.click(*TERMINAL_UI_POS)
    elif app == 'mobax':
        pyautogui.click(*MBXTERM_UI_POS)


def wait_mobax():       # <--- State (1)
    '''
    Check every 1.5 seconds if the file is not empty
    '''
    while True:
        f_size = Path(MOBAX_LOG_PATH).stat().st_size
        if f_size > 0: break 
        time.sleep(1.5)
        print('waiting...')

        pattern = re.compile(r'last action: [a-z]\d+')
    with open(MOBAX_LOG_PATH, 'r+') as f:
        result = pattern.findall(f.read())[0]
        f.truncate(0)
        print(f'[out]: {result}')
        pyperclip.copy(result)


def input_ludii():      # <--- State (2)
    coord = pyperclip.paste()
    coord = f'{coord.upper()}/0' # Ludii coordinate input format 
    pyperclip.copy(coord)
    goto_('ludii')
    pyautogui.hotkey('alt', 's')
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.hotkey('backspace')
    pyautogui.hotkey('enter')


def wait_ludii():       # <--- State (3)
    global current_mv
    global old_result
    if START_AUTO_AT_MV == current_mv:
        while True:     # keep copy until the new value entered
            pyautogui.moveTo(*BEGIN_LINE_POS) # beginning of the line
            pyautogui.mouseDown()
            pyautogui.drag(MOVE_TEXT_LENGTH,  0, duration=1, button='left')
            pyautogui.hotkey('ctrl', 'c')
            pattern = re.compile('[A-Z]\d+/0\)$') # D1/0)
            result = pattern.findall(pyperclip.paste())[0][:-3].lower()
            if result != old_result: 
                print(f'[in]: {result}')
                pyperclip.copy(result)
                break
            time.sleep(1.5)
            print('waiting...')
    else:
        current_mv += 1
        goto_('terminal')
        coordinate = input('[input]: ')
        print(f'[in]: {coordinate}')
        pyperclip.copy(coordinate)


def input_mobax():      # <--- State (4)
    goto_('mobax')
    pyautogui.rightClick() # Config copy in MobaXterm
    pyautogui.hotkey('enter')


def test():
    check_mouse_position()
    # input_ludii()
    # wait_mobax()
    # input_mobax()
    # wait_ludii()

def check_mouse_position():
    while True:
        ms_pos = pyautogui.position()
        print(ms_pos)
        if ms_pos.x == 0: break


if __name__ == '__main__':
    check_mouse_position()