# this class can hole 1 item for a specific tick duration before it is ready to be taken off the stack

import logging

log = logging.getLogger(__name__)

# import item from resources.item
from resources.item import Item
from resources.object import Object

# declare a class to represent a stack slot
class StackSlot(Object):
    def __init__(self, item, tick_duration=100, tick_production_rate=1):
        super().__init__()
        self.name = "StackSlot"+str(self.id)
        self.item = item # Item to store for tick_count
        self.tick_count = 0 # number of ticks to keep item in this slot before allowing it to be taken off
        self.tick_duration = tick_duration # number of ticks to keep item in this slot before allowing it to be taken off
        self.tick_production_rate = tick_production_rate # increase tick_count by tick_consumption_rate
        self.ready = False # flag to indicate if the item is ready to be taken off the stack
        #log.debug(("StackSlot created with item: " + str(self.item) + " and _tick_duration: " + str(self.tick_duration))
        #log.debug((str(self))
    
    def process(self):
        if self.ready:
            #log.debug(("StackSlot with item: " + str(self.item) + " is ready")
            return
        if self.tick_count >= self.tick_duration:
            self.ready = True
            #log.debug(("StackSlot with item: " + str(self.item) + " is ready")
        else:
            self.tick_count += self.tick_production_rate
            #log.debug(("StackSlot with item: " + str(self.item) + " is processing")
    
    def __str__(self):
        return "{}(id:{} with item: {} progress {}/{})".format(self.name, str(self.id), self.item, self.tick_count, self.tick_duration)
    
    def delete(self):
        self.deleted = True
        #log.debug(("StackSlot with item: " + str(self.item) + " is deleted")
    
    def isReady(self):
        return self.ready
    
    def getItem(self):
        return self.item