import cx_Freeze
from cx_Freeze import *
import os

os.environ['TCL_LIBRARY'] = "C:\Python27\tcl\tcl8.5"
os.environ['TK_LIBRARY'] = "C:\Python27\tcl\tk8.5"

build_options = {'packages': ['pygame'], 'excludes': ['tkinter']}

base = None
if (sys.platform == "win32"):
    base = "Win32GUI"

setup(
    name = "ratgame",
    version = "1.0",
    options = {'build_exe': build_options},
    executables=[Executable("ratgame.py", base=base)]
)
print("Game frozen successfully!")