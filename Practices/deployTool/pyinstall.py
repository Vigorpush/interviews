
import  os
if __name__ == '__main__':
    from PyInstaller.__main__ import run
    opts=['mainwindow.py','-w','--icon=logo.ico']
    run(opts)