from enum import Enum
import logging

from resources.buildings.building import Building
from resources.flag import Flag

log = logging.getLogger(__name__)

class ProductionCategory(Enum):
    PRIMARY=1 # ie. WOODCUTTER, STONECUTTER
    SECONDARY=2 # ie. SAWMILL
    TERTIARY=3 # ie. IRONSMELTER

# define an enum for the production building type
class ProductionType(Enum):
    WOODCUTTER=1
    STONECUTTER=2
    SAWMILL=3

# define a class for a production building
class ProductionBuilding(Building):
    # override the init function
    def __init__(self, category, type, location=None):
        super().__init__(location)
        # define a name for the production building
        self.name = "ProductionBuilding"+str(self.id)       
        self.category = category
        self.type = type
        
        # TODO
        # Add stack of items to consume. Can be multiple items that are consumed together
        # Add output item when production is complete
        # Add tick duration for production to complete
        
        log.debug("ProductionBuilding created with id: " + str(self.id))
        log.debug(str(self))
    
    # override the process function
    def process(self):
        if self.deleted:
            #log.debug("ProductionBuilding with id: " + str(self.id) + " is deleted, skip processing")
            return
        # call the process function of the base class
        super().process()
        
        log.debug("ProductionBuilding with id: " + str(self.id) + " is processing")
        
    # define a string representation of the production object
    def __str__(self):
        return "{}(id:{} at Flag {} with category {} and type {} at {})".format(self.name, str(self.id), self.flag.id, self.category.name, self.type.name, self.location)