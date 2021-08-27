"""
Author: Saitako
GUI automation for Ludii and Polygame
""" 
from auto.tools import (
    HexCoordTranslate,
)

from auto.sc_control import (
    input_ludii,
    input_mobax,
    wait_ludii,
    wait_mobax,
    test,
)

EXEC_CMD = 'ldpg_t'
SRC_INPUT = ['polygame', 'ludii']
P_OR_O = {'polygame': 'player', 'ludii': 'opponent'}



def Hex():
    move_first = input('move first?: [yes] or [no]\n')
    board_size = input('board size: 13 or 19\n')
    isrc_index = 0 if move_first == 'yes' else 1
    print('Type "exit" to exit')
    while True:
        src = SRC_INPUT[isrc_index % 2]
        print(f'Turn: {P_OR_O[src]}')
        coordinate = input('[in]: ')
        if coordinate == 'exit': 
            break
        output_coord = HexCoordTranslate(board_size, src, coordinate)
        print(f'[out]: {output_coord}')
        # copy2clip(f'{output_coord}\\0')
        if output_coord == 'Not found!': 
            continue
        input_ludii()
        isrc_index += 1

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