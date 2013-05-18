class Viewport(object):
    def __init__(self, limits = (0,0,0,0)):
        self.x_start    = limits[0]
        self.x_end      = limits[1]
        self.y_start    = limits[2]
        self.y_end      = limits[3]
    
    def set_size(self, width, height):
        self.x_end      = self.x_start + width
        self.y_end      = self.y_start + height
        
