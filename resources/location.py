import logging

log = logging.getLogger(__name__)

# define a class for a location
class Location():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    @staticmethod
    def distance(location1, location2):
        # return the straight line distance between two locations
        return ((location1.x - location2.x)**2 + (location1.y - location2.y)**2 + (location1.z - location2.z)**2)**0.5
        
    @staticmethod
    def midpoint(location1, location2):
        # return the midpoint between two locations
        return Location((location1.x + location2.x)/2, (location1.y + location2.y)/2, (location1.z + location2.z)/2)

    def __str__(self):
        return "[{},{},{}]".format(self.x, self.y, self.z)