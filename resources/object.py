import logging

log = logging.getLogger(__name__)

# define a class to represent an object in the game with an id and a process function
class Object:
    counter = 0
    def __init__(self, location=None):
        Object.counter += 1
        self.id = Object.counter
        self.location = location
        self.deleted = False
        # log.debug("Object created with id: " + str(self.id))
    
    def process(self):
        # log.debug("Object with id: " + str(self.id) + " is processing")
        # do nothing
        pass

    # define a string representation of the object
    def __str__(self):
        return "{}(id:{} at {})".format(self.name, str(self.id), self.location)
    
    def delete(self):
        self.deleted = True
        log.debug("Object with id: " + str(self.id) + " is deleted")
