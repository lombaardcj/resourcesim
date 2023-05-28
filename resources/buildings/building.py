import logging
# import Object from resources.object
from resources.object import Object

# import flag from resources.flag
from resources.flag import Flag

log = logging.getLogger(__name__)

# inherit from the base class Object
class Building(Object):
    # override the init function
    def __init__(self, location):
        super().__init__(location)
        # define a name for the building
        self.name = "Building"+str(self.id)
        self.flag = Flag(location) # create a flag at the location of the building
        #log.debug("Building created with id: " + str(self.id))
    
    # override the process function
    def process(self):
        if self.deleted:
            ##log.debug("Building with id: " + str(self.id) + " is deleted, skip processing")
            return
        # call the process function of the base class
        super().process()
        
        #log.debug("Building with id: " + str(self.id) + " is processing")
        
    # define a string representation of the building object
    def __str__(self):
        return "{}(id:{})".format(self.name, str(self.id))
