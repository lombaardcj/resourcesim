import threading
import logging
import sys
import time

# import local modules
from gameengine import GameState
engine = GameState(startup_tick_duraction=1)

# initialise the logger
logging.basicConfig(stream=sys.stdout,level=logging.DEBUG)
log = logging.getLogger(__name__)
log.info("Initialising logger")

def loop():
    while True:
        engine.process()

        # sleep for the tick duration
        time.sleep(engine.get_tick_duration())

if __name__ == "__main__":
    t = threading.Thread(target=loop)
    t.start()
    t.join()