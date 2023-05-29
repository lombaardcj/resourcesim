import logging

# import stackslot from resources.stackslot
from resources.stackslot import StackSlot
from resources.object import Object
from resources.location import Location

log = logging.getLogger(__name__)

# create a class to represent a path link
# the path link is a link between two flags

class PathLink(Object):
    def __init__(self, flagA, flagB, capacity=1):
        super().__init__(Location.midpoint(flagA.location, flagB.location))
        self.flagA = flagA
        self.flagB = flagB
        self.name = "PathLink"+str(self.id)
        self.item_stack_AB = [] # Keep list of all items transported from flagA to flagB
        self.item_stack_BA = [] # Keep list of all items transported from flagB to flagA
        self.capacity = capacity # maximum number of items that can be transported at once
        self.speed = Location.distance(flagA.location, flagB.location) * 500 # speed of the pathlink
        #log.debug(("PathLink created with id: " + str(self.id))
        log.debug(self)
    
    def process(self):
        if self.deleted:
            ##log.debug(("PathLink with id: " + str(self.id) + " is deleted, skip processing")
            return
        # call the process function of the base class
        super().process()
        
        #log.debug(("PathLink with id: " + str(self.id) + " is processing")
        
        # process the item stack AB
        if len(self.item_stack_AB) > 0:
            for item in self.item_stack_AB:
                item.process()
                if item.isReady():
                    # first check if the flagB is full
                    if self.flagB.isFull():
                        #log.debug(("Flag {} is full, cannot push item: {} from PathLink with id: {}".format(self.flagB.id, item.id, self.id))
                        continue
                    
                    # pop the item from the item stack
                    item = self.item_stack_AB.pop(0)
                    # push the item to the item stack of flagB
                    self.flagB.push_item(item)
                    #log.debug(("Item {} pushed to Flag {} from PathLink with id: {}".format(item.id, self.flagB.id, self.id))
        
        # process the item stack BA
        if len(self.item_stack_BA) > 0:
            for item in self.item_stack_BA:
                item.process()
                if item.isReady():
                    # first check if the flagA is full
                    if self.flagA.isFull():
                        #log.debug(("Flag {} is full, cannot push item: {} from PathLink with id: {}".format(self.flagA.id, item.id, self.id))
                        continue
                    
                    # pop the item from the item stack
                    item = self.item_stack_BA.pop(0)
                    # push the item to the item stack of flagA
                    self.flagA.push_item(item)
                    #log.debug(("Item {} pushed to Flag {} from PathLink with id: {}".format(item.id, self.flagA.id, self.id))
    
    def __str__(self):
        return "{}(id:{} between Flag {} and Flag {} with speed {} at {})".format(self.name, str(self.id), self.flagA.id, self.flagB.id, self.speed, self.location)
        
    def push_item_AtoB(self, item):
        # check if the pathlink is full
        if len(self.item_stack_AB) >= self.capacity:
            #log.debug(("PathLink with id: " + str(self.id) + " is full, cannot push item: " + str(item))
            return
        # push the item to the item stack
        self.item_stack_AB.append(StackSlot(item))
        #log.debug(("Item {} pushed to PathLink with id: {}".format(item.id, self.id))
    
    def push_item_BtoA(self, item):
        # check if the pathlink is full
        if len(self.item_stack_BA) >= self.capacity:
            #log.debug(("PathLink with id: " + str(self.id) + " is full, cannot push item: " + str(item))
            return
        # push the item to the item stack
        self.item_stack_BA.append(StackSlot(item))
        #log.debug(("Item {} pushed to PathLink with id: {}".format(item.id, self.id))
    
