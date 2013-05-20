class Position:
    def __init__(self, x = 0 , y= 0):
        self.x = x
        self.y = y

class Size:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
class Limits:
    def __init__(self,limits = (0,0,0,0)):
        self.x_start    = limits[0]
        self.x_end      = limits[1]
        self.y_start    = limits[2]
        self.y_end      = limits[3]
    
    def set_limits(self, limits):
        self.x_start    = limits[0]
        self.x_end      = limits[1]
        self.y_start    = limits[2]
        self.y_end      = limits[3]
        
    def get_xend_limit(self):
        return min(self.position.x + self.size.width, self.size.width-1)

    def get_yend_limit(self):
        return min(self.position.x + self.size.width, self.size.height-1)