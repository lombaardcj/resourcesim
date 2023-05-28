from enum import Enum
import logging

from resources.buildings.building import Building

log = logging.getLogger(__name__)

class StorageCategory(Enum):
    PRIMARY=1 # ie. Headquarters, Storehouse

class StorageType(Enum):
    HEADQUARTERS=1
    STOREHOUSE=2

# define a class for a storage building
class StorageBuilding(Building):
    # override the init function
    def __init__(self, category, type, location=None):
        super().__init__(location)
        # define a name for the storage building
        self.name = "StorageBuilding"+str(self.id)
        self.category = category
        self.type = type
        self.item_stack = [] # create a stack of Item instances that are stored in the storage building
        log.debug("StorageBuilding created with id: " + str(self.id))
        log.debug(self)
    
    # override the process function
    def process(self):
        if self.deleted:
            #log.debug("StorageBuilding with id: " + str(self.id) + " is deleted, skip processing")
            return
        # call the process function of the base class
        super().process()
        
        log.debug("StorageBuilding with id: " + str(self.id) + " is processing")
        
    # define a string representation of the storage object
    def __str__(self):
        return "{}(id:{} with category {} and type {} at {})".format(self.name, str(self.id), self.category.name, self.type.name, self.location)
