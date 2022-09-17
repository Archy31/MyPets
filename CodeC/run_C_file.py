import os
from pathlib import Path


def run_C(name_prog: str, add_path: str=''):

    path_cfile = os.path.dirname(__file__) + add_path

    os.chdir(path_cfile)
    if not os.path.isdir(name_prog + '.exe'):
        cmd_to_compile = f'gcc {name_prog}.C -o {name_prog}.exe'
        os.system(cmd_to_compile)

        cmd_to_run = f'./{name_prog}.exe'
        return os.system(cmd_to_run)

    else:
        cmd_to_run = f'./{name_prog}.exe'
        return os.system(cmd_to_run)
