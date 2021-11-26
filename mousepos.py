def install_and_import(package):
    import importlib
    try:
        importlib.import_module(package)
    except ImportError:
        import pip
        pip.main(['install', package])
    finally:
        globals()[package] = importlib.import_module(package)

install_and_import ('pyautogui')
import sys
import time
y=0
while True:
    x=pyautogui.position()
    if x!=y:
        sys.stdout.write ('\r'+ str(x)+ ' ' *10),
    y=x
    time.sleep(0.01)
