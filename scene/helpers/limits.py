from position import Position

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
        
        self.x_start    = self.get_x_start_limit()
        self.x_end      = self.get_x_end_limit()
        self.y_start    = self.get_y_start_limit()    
        self.y_end      = self.get_y_end_limit()
        
    def get_x_start_limit(self):
        return min(self.position.x, self.size.width-1)
    
    def get_y_start_limit(self):
        return min(self.position.y, self.size.height-1)
    
    def get_x_end_limit(self):
        if(self.position.x + self.size.width < 0):
            return 0
        return min(self.position.x + self.size.width, self.size.width-1)

    def get_y_end_limit(self):
        if(self.position.y + self.size.height< 0):
            return 0
        return min(self.position.y + self.size.height, self.size.height-1)
    
    def get_positions_available(self):
        return [Position(tx,ty) for tx in xrange(self.x_start, self.x_end) for ty in xrange(self.y_start, self.y_end)]
                
                