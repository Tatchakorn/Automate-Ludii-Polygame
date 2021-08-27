"""
Author: Saitako
GUI automation for Ludii and Polygame
""" 

from auto.tools import (
    HexCoordTranslate,
    set_board_size,
)

from auto.sc_control import (
    input_ludii,
    input_mobax,
    wait_ludii,
    wait_mobax,
    test,
    set_translation,
)


def Hex():
    move_first = input('move first?: [yes] or [no]\n')
    board_size = input('board size: 13 or 19\n')
    set_board_size(board_size)
    set_translation(True)
    
    if move_first == 'yes':
        while True:
            wait_mobax()
            input_ludii()
            wait_ludii()
            input_mobax()
    else:
        while True:
            wait_ludii()
            input_mobax()
            wait_mobax()
            input_ludii()

def Havana10():
    move_first = input('move first?: [yes] or [no]\n')
    if move_first == 'yes':
        while True:
            wait_mobax()
            input_ludii()
            wait_ludii()
            input_mobax()
    else:
        while True:
            wait_ludii()
            input_mobax()
            wait_mobax()
            input_ludii()

def test_sc_ctrl():
    test()

if __name__ == '__main__':
    # Havana10()
    test_sc_ctrl()