class Limits:
    def __init__(self, position, size):
        self.position = position
        self.size = size
        
        self.x_start    = position.x
        self.x_end      = self.get_x_end_limit()
        self.y_start    = position.y       
        self.y_end      = self.get_y_end_limit()
    
    def set_position(self, position):
        self.position = position
        
        self.x_start    = position.x
        self.x_end      = self.get_x_end_limit()
        self.y_start    = position.y       
        self.y_end      = self.get_y_end_limit()
        
    def get_x_end_limit(self):
        return min(self.position.x + self.size.width, self.size.width-1)

    def get_y_end_limit(self):
        return min(self.position.x + self.size.width, self.size.height-1)