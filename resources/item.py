from enum import Enum

import logging
# import Object from resources.object
from resources.object import Object

log = logging.getLogger(__name__)

# define a enum for the item category
class ItemCategoryEnum(Enum):
    RESOURCE=1
    TOOL=2

class ItemCategory(Enum):
    WOOD=ItemCategoryEnum.RESOURCE
    STONE=ItemCategoryEnum.RESOURCE
    PLANK=ItemCategoryEnum.RESOURCE
    AXE=ItemCategoryEnum.TOOL
    SAW=ItemCategoryEnum.TOOL

# define the type of item i.e WOOD, STONE, IRON under category RESOURCE
# define the type of item i.e AXE, SAW, HAMMER under category TOOL
class ItemType(Enum):
    # define the resource types
    WOOD=1
    STONE=2
    PLANK=3
    
    # define the tool types
    AXE=100
    SAW=101


# inherit from the base class Object
class Item(Object):
    # override the init function
    def __init__(self, type, location=None):
        super().__init__(location)
        # define a name for the item
        self.name = "Item"+str(self.id)
        self.type = type
        self.category = ItemCategory[type.name].value
        #log.debug("Item created with id: {} with category {} and type {}".format(str(self.id),str(self.category), str(self.type)))
        #log.debug(self)
    
    # override the process function
    def process(self):
        #log.debug(self)
        if self.deleted:
            #log.debug("Item with id: " + str(self.id) + " is deleted, skip processing")
            return
        # call the process function of the base class
        super().process()
        
        #log.debug("Item with id: " + str(self.id) + " is processing")
        log.debug(self)
        
    # define a string representation of the item object
    def __str__(self):
        return "{}(id:{} with category {} and type {} at {})".format(self.name, str(self.id), self.category.name, self.type.name, self.location)