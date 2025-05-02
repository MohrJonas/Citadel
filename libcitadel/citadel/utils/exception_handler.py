import sys
from tkinter.messagebox import showerror
from traceback import format_tb
from os import linesep

def install_exception_handler() -> None:
    def on_exception(_, value, traceback) -> None:
        showerror(value, str.join(linesep, format_tb(traceback)))
    sys.excepthook = on_exception