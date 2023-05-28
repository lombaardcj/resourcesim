import logging
# import Object from resources.object
from resources.object import Object

# import item from resources.item
from resources.item import Item

log = logging.getLogger(__name__)

# A Flag object is used to indicate where items can be temporarily placed
# A maximum of 8 objects can be kept at this location
# A building will always have a flag object

# define a class for a Flag object
class Flag(Object):
    # override the init function
    def __init__(self, location):
        super().__init__(location)
        # define a name for the flag
        self.name = "Flag"+str(self.id)
        self.item_stack = [] # Keep list of all items stored at this flag
        log.debug("Flag created with id: " + str(self.id))
        log.debug(self)
    
    # override the process function
    def process(self):
        if self.deleted:
            #log.debug("Flag with id: " + str(self.id) + " is deleted, skip processing")
            return
        # call the process function of the base class
        super().process()
        
        log.debug("Flag with id: " + str(self.id) + " is processing")
        
    # define a string representation of the flag object
    def __str__(self):
        return "{}(id:{} at {})".format(self.name, str(self.id), self.location)
    
    def delete(self):
        super().delete()
        self.building.flag = None
        log.debug("Flag with id: " + str(self.id) + " is deleted")

    def push_item(self, item):
        self.item_stack.append(item.id)
        log.debug("Item with id: " + str(item.id) + " added to flag with id: " + str(self.id))
    
    def pop_item(self, item):
        # remove the item from the item stack that matches the item id
        # first check if the item id is in the item stack
        if item.id in self.item_stack:
            self.item_stack.remove(item.id)
            log.debug("Item with id: " + str(item.id) + " removed from flag with id: " + str(self.id))
        else:
            log.debug("Item with id: " + str(item.id) + " not found in flag with id: " + str(self.id))