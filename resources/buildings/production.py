from enum import Enum
import logging

# define local modules
from resources.buildings.building import Building
from resources.flag import Flag

from resources.item import Item
from resources.item import ItemType

from resources.stackslot import StackSlot

log = logging.getLogger(__name__)

class ProductionCategoryEnum(Enum):
    PRIMARY=1 # ie. WOODCUTTER, STONECUTTER
    SECONDARY=2 # ie. SAWMILL
    TERTIARY=3 # ie. IRONSMELTER

class ProductionCategory(Enum):
    WOODCUTTER=ProductionCategoryEnum.PRIMARY
    STONECUTTER=ProductionCategoryEnum.PRIMARY
    SAWMILL=ProductionCategoryEnum.SECONDARY

# define an enum for the production building type
class ProductionType(Enum):
    WOODCUTTER=1
    STONECUTTER=2
    SAWMILL=3
    
# define an enum for the building production speed
class ProductionSpeed(Enum):
    WOODCUTTER=10
    STONECUTTER=10
    SAWMILL=5

# define an enum for the building production capacity
class ProductionCapacity(Enum):
    WOODCUTTER=1
    STONECUTTER=1
    SAWMILL=1

# define the type of item to produce by building type
class ProductionItem(Enum):
    WOODCUTTER=ItemType.WOOD
    STONECUTTER=ItemType.STONE
    SAWMILL=ItemType.PLANK

# create a production order class that defines the raw items to consume and the output item
# A ProductionOrder defines the amount of input_item_types required to produce 1 output_item_type
class ProductionOrder():
    def __init__(self, input_item_types, output_item_type, tick_duration=100):
        self.input_item_types = input_item_types
        self.output_item_type = output_item_type
        self.tick_duration = tick_duration
    
    def __str__(self):
        return "ProductionOrder(input_item_types: {}, output_item_type: {}, tick_duration: {})".format(self.input_item_types, self.output_item_type, self.tick_duration)

# define a class for a production building
class ProductionBuilding(Building):
    # override the init function
    def __init__(self, type,location=None):
        super().__init__(location)
        # define a name for the production building
        self.name = "ProductionBuilding"+str(self.id)       
        self.type = type
        # define category based on the production type
        # lookup the categorey based on the production type
        self.category = ProductionCategory[type.name].value
        
        self.materials_stack = [] # Keep list of all items consumed at this building
        
        self.production_order = None
        # define the production order based on the building type
        if self.type == ProductionType.SAWMILL:
            self.production_order = ProductionOrder(input_item_types=[ItemType.WOOD], output_item_type=ItemType.PLANK, tick_duration=ProductionSpeed[type.name].value)
        
        self.production_stack = [] # Keep list of all items produced at this building
        self.capacity = ProductionCapacity[type.name].value # maximum number of items that can be produced at this building
        # Add stack of items to consume. Can be multiple items that are consumed together
        # Add output item when production is complete
        # Add tick duration for production to complete
        
        #log.debug("ProductionBuilding created with id: " + str(self.id))
        #log.debug(str(self))
    
    # override the process function
    def process(self):
        if self.deleted:
            ##log.debug("ProductionBuilding with id: " + str(self.id) + " is deleted, skip processing")
            return
        # call the process function of the base class
        super().process()
        
        #log.debug("ProductionBuilding with id: " + str(self.id) + " is processing")
        
        # process the production stack
        if len(self.production_stack) > 0:
            #log.debug("Production stack is not empty, process the production stack")
            for item in self.production_stack:
                item.process()
                log.debug("Processed item: " + str(item))
                if item.isReady():
                    # first check if the building flag is full
                    if self.flag.isFull():
                        log.debug("Flag {} is full, cannot push item: {} from ProductionBuilding with id: {}".format(self.flag.id, item.id, self.id))
                        continue
                    
                    # pop the item from the production stack
                    item = self.production_stack.pop(0).getItem()
                    # push the item to the item stack of flag
                    self.flag.push_item(item)
                    log.debug("Item {} pushed to Flag {} from ProductionBuilding with id: {}".format(item.id, self.flag.id, self.id))
        else:
            # production stack is empty, check if there is a production order that can be processed
            #log.debug("Production stack is empty, check if there is a production order that can be processed")
            if self.production_order is not None:
                ##log.debug("")
                can_process = False
                # copy the material stack items to a temporary list and remove the items from the material stack
                # as the items are match the production order
                copy_materials_stack = self.materials_stack.copy()
                
                #log.debug("Make a copy of the material stack")
                # print the material stack
                #log.debug("Items in material stack: ")
                for item in copy_materials_stack:
                    #log.debug(str(item))
                    pass
                
                # check if the material stack has the required input items and remove them from the material stack
                # if the production order item cannot be matched, then the production order cannot be processed
                for input_item in self.production_order.input_item_types:
                    #log.debug("Check if the material stack has the required input item: " + str(input_item))
                    
                    # check if the input item is in the material stack
                    if input_item in [item.type for item in copy_materials_stack]:
                        # find the index of the input item in the material stack
                        index = [item.type for item in copy_materials_stack].index(input_item)
                        
                        #log.debug("The material stack has the required input item: " + str(input_item))
                        # remove the input item from the material stack
                        copy_materials_stack.pop(index)
                    else:
                        # the production order cannot be processed
                        #log.debug("ProductionBuilding with id: " + str(self.id) + " cannot process production order: " + str(self.production_order))
                        return
                    
                    # the production order can be processed
                    can_process = True
                    break;
                
                # check if the production order can be processed
                if can_process:
                    for input_item in self.production_order.input_item_types:
                        #log.debug("Remove the input item: " + str(input_item) + " from the material stack")
                        # remove the input item from the material stack
                        if input_item in [item.type for item in self.materials_stack]:
                            # find the index of the input item in the material stack
                            index = [item.type for item in self.materials_stack].index(input_item)
                            #log.debug("The material stack has the required input item: " + str(input_item) + " at index: " + str(index))
                            # remove the input item from the material stack
                            self.materials_stack.pop(index)
                        else:
                            log.error("ProductionBuilding with id: " + str(self.id) + " cannot process production order: " + str(self.production_order))
                            #exit the current for loop
                            return
                    
                    # create the output item on the production stack
                    stack_slot = StackSlot(item=Item(self.production_order.output_item_type, location=self.location), tick_duration=self.production_order.tick_duration)
                    self.production_stack.append(stack_slot)
                    log.debug("Added stackslot for output item to start producing" + str(stack_slot))

    # add item to material stack with location of the production building
    def addMaterial(self, item):
        item.location = self.location
        #log.debug("Location of item: " + str(item) + " is set to: " + str(self.location))
        #log.debug("Added item: " + str(item) + " to ProductionBuilding with id: " + str(self.id))
        self.materials_stack.append(item)

    # define a string representation of the production object
    def __str__(self):
        return "{}(id:{} at Flag {} with category {} and type {} at {})".format(self.name, str(self.id), self.flag.id, self.category.name, self.type.name, self.location)