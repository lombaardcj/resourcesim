import logging

log = logging.getLogger(__name__)

# create a class to represent a path link
# the path link is a link between two flags

class PathLink(Object):
    def __init__(self, flagA, flagB):
        super().__init__(Location.midpoint(flag1.location, flag2.location))
        self.flagA = flag1
        self.flagB = flag2
        self.name = "PathLink"+str(self.id)
        self.item_stack = [] # Keep list of all items stored at this pathlink
        log.debug("PathLink created with id: " + str(self.id))
        log.debug(str(self))
    
    def process(self):
        if self.deleted:
            #log.debug("PathLink with id: " + str(self.id) + " is deleted, skip processing")
            return
        # call the process function of the base class
        super().process()
        
        log.debug("PathLink with id: " + str(self.id) + " is processing")
    
    def __str__(self):
        return "{}(id:{} between Flag {} and Flag {} at {})".format(self.name, str(self.id), self.flagA.id, self.flagB.id, self.location)