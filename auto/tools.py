"""
Author: Saitako
Ludii Automation CLI 
Automatically copy output to clipboard
[WARNING] only works on Windows
"""
import subprocess

EXE_CMD = 'coord_lookup'
BOARD_SIZE = 0

def HexCoordTranslate(src: str, coordinate: str) -> str:
    """
    src: "ludii" or "polygame"
    """
    cmd_list = [EXE_CMD, BOARD_SIZE, src, coordinate]
    proc = subprocess.run(
        cmd_list,
        shell=True,
        capture_output=True,
        text=True
    )
    return proc.stdout

def set_board_size(b_size: int):
    global BOARD_SIZE
    BOARD_SIZE = b_size

if __name__ == '__main__':
    ...