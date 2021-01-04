import os
import shutil
from typing import List


def rmfiles(files: List[str], basedir: str = "."):
    for file in files:
        os.remove(os.path.join(basedir, file))
        pass
    pass


def rmdir(dirs: List[str], basedir: str = "."):
    for directory in dirs:
        if os.path.isdir(directory):
            shutil.rmtree(os.path.join(basedir, directory))
            pass
        pass
    pass
