import logging

# import item type enum
from resources.item import Item
from resources.item import ItemCategory
from resources.item import ItemType

from resources.buildings.production import ProductionBuilding
from resources.buildings.production import ProductionCategory
from resources.buildings.production import ProductionType

from resources.buildings.storage import StorageBuilding
from resources.buildings.storage import StorageCategory
from resources.buildings.storage import StorageType

# import the WorkOrder class from resources/workorder.py
from resources.workorder import WorkOrder

# import location from resources.location
from resources.location import Location

log = logging.getLogger(__name__)

class GameState():
    _tick = 0 # global variable to keep track of the number of times the process function is called
    def __init__(self, startup_tick_duraction=1):
        self._tick_duration = startup_tick_duraction # duration of a tick in seconds
        
        self._flag_stack = [] # create a stack of Flag instances
        self._item_stack = [] # create a stack of Item instances
        
        self._production_building_stack = [] # create a stack of Building instances
        self._storage_building_stack = [] # create a stack of Building instances

        self._workorder_stack = [] # create a stack of WorkOrder instances

    def init_game(self):
        log.debug("Initialising game objects")
        
        # create production buildings
        self._production_building_stack.append(ProductionBuilding(category=ProductionCategory.PRIMARY, type=ProductionType.WOODCUTTER, location=Location(10,10,0)))  
        # get the last building in the production building stack
        self._flag_stack.append(self._production_building_stack[-1].flag)
        
        self._production_building_stack.append(ProductionBuilding(category=ProductionCategory.PRIMARY, type=ProductionType.STONECUTTER, location=Location(10,9,0)))
        self._flag_stack.append(self._production_building_stack[-1].flag)
        
        self._production_building_stack.append(ProductionBuilding(category=ProductionCategory.SECONDARY, type=ProductionType.SAWMILL, location=Location(5,5,0)))
        self._flag_stack.append(self._production_building_stack[-1].flag)
        
        # create storage buildings
        self._storage_building_stack.append(StorageBuilding(category=StorageCategory.PRIMARY, type=StorageType.HEADQUARTERS, location=Location(0,0,0)))
        self._flag_stack.append(self._storage_building_stack[-1].flag)
        
        self._storage_building_stack.append(StorageBuilding(category=StorageCategory.PRIMARY, type=StorageType.STOREHOUSE, location=Location(10,0,0)))
        self._flag_stack.append(self._storage_building_stack[-1].flag)
        
        
    def process(self):
        GameState._tick += 1
        log.debug("Advanced the game Tick to: " + str(GameState._tick))
        
        # check if the start of game i.e. _tick == 1
        if GameState._tick == 1:
            self.init_game()
            
        # call the process function of the production building instance
        for building in self._production_building_stack:
            building.process()
            
        # call the process function of the storage building instance
        for building in self._storage_building_stack:
            building.process()
        
    
        
        # call the process function of the workorder instance
        for workorder in self._workorder_stack:
            workorder.process()
            
        if GameState._tick % 10 == 0:
            # call the process function of the production building instance
            for building in self._production_building_stack:
                building.process()
    
    @staticmethod
    def get_tick():
        return GameState._tick
        
    def set_tick_duration(self, duration):
        self._tick_duration = duration
    def get_tick_duration(self):
        return self._tick_duration