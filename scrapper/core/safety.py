import threading
import keyboard
from core.logger import logger

KILL_FLAG = False

def kill_listener():
    global KILL_FLAG
    logger.info("Kill switch armed: CTRL + SHIFT + K")

    keyboard.wait("ctrl+shift+k")
    KILL_FLAG = True
    logger.critical("🔥 KILL SWITCH ACTIVATED 🔥")

def start_kill_switch():
    t = threading.Thread(target=kill_listener, daemon=True)
    t.start()
