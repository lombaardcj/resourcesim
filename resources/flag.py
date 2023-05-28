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
    def __init__(self, location, capacity=3):
        super().__init__(location)
        # define a name for the flag
        self.name = "Flag"+str(self.id)
        self.item_stack = [] # Keep list of all items stored at this flag
        self.capacity = capacity # maximum number of items that can be stored at this flag
        #log.debug(("Flag created with id: " + str(self.id))
        #log.debug((self)
    
    # override the process function
    def process(self):
        if self.deleted:
            ##log.debug(("Flag with id: " + str(self.id) + " is deleted, skip processing")
            return
        # call the process function of the base class
        super().process()
        
        #log.debug(("Flag with id: " + str(self.id) + " is processing")
        log.debug(self)
        
    # define a string representation of the flag object
    def __str__(self):
        # concatenate all item types in the item_stack with comma
        item_types = ""
        for item in self.item_stack:
            item_types += str(item.type) + ","
        return "{}(id:{} {}/{} with item_types {} at {})".format(self.name, str(self.id), len(self.item_stack), self.capacity, item_types, self.location)
    
    def delete(self):
        super().delete()
        self.building.flag = None
        #log.debug(("Flag with id: " + str(self.id) + " is deleted")

    def push_item(self, item):
        # add location of flag to item
        item.location = self.location
        self.item_stack.append(item)
        #log.debug(("Item with id: " + str(item.id) + " added to flag with id: " + str(self.id))
    
    def pop_item(self, item):
        # remove the item from the item stack that matches the item
        self.item_stack.remove(item)
        log.debug("Item with id: " + str(item.id) + " removed from flag with id: " + str(self.id))
    
    def isFull(self):
        if len(self.item_stack) >= self.capacity:
            return True
        else:
            return False