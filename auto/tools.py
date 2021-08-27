"""
Author: Saitako
Ludii Automation CLI 
Automatically copy output to clipboard
[WARNING] only works on Windows
"""
import subprocess


def HexCoordTranslate(exe_name: str, board_size: int, src: str, coordinate: str) -> str:
    cmd_list = [exe_name, board_size, src, coordinate]
    proc = subprocess.run(
        cmd_list,
        shell=True,
        capture_output=True,
        text=True
    )
    return proc.stdout


if __name__ == '__main__':
    ...