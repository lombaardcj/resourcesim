import logging
# import Object from resources.object
from resources.object import Object

log = logging.getLogger(__name__)

# inherit from the base class Object

class WorkOrder(Object):
    # override the init function
    def __init__(self):
        super().__init__()
        # define a name for the work order
        self.name = "WorkOrder"+str(self.id)
        log.debug("WorkOrder created with id: " + str(self.id))
        log.debug(self)
    
    # override the process function
    def process(self):
        if self.deleted:
            #log.debug("WorkOrder with id: " + str(self.id) + " is deleted, skip processing")
            return
        # call the process function of the base class
        super().process()
        
        log.debug("WorkOrder with id: " + str(self.id) + " is processing")
        
    # define a string representation of the workorder object
    def __str__(self):
        return "{}(id:{})".format(self.name, str(self.id))
    
