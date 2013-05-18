import data_types

class Viewport(object):
    def __init__(self, position  , size ):
        self.position = position
        self.size = size
        self.limits = data_types.Limits((self.position.x,self.position.y,self.position.x + self.size.width ,self.position.y + self.size.height))
    
    def set_size(self, width, height):
        self.size = size
        
    def set_position(self, position):
        self.position = position
        
    def set_position(self, x, y):
        self.position.x = x
        self.position.y = y
        self.limits.set_limits((self.position.x,self.position.y,self.position.x + self.size.width ,self.position.y + self.size.height))
        
        return self.limits
    
