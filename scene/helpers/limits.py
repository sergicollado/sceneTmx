from position import Position

class Limits:
    def __init__(self, position, map_size , window_size, tile_size):
        self.position = position
        self.map_size = map_size
        self.window_size = window_size
        self.tile_size = tile_size
        
        self.processing_limits()
    
    def set_position(self, position):
        self.position = position

        self.processing_limits()
    
    def processing_limits(self):
        self.x_start    = self.get_x_start_limit()
        self.x_end      = self.get_x_end_limit()
        self.y_start    = self.get_y_start_limit()    
        self.y_end      = self.get_y_end_limit()
        
        
    def get_x_start_limit(self):
        if(self.position.x  < 0):
            return 0
        
        return min(self.position.x,self.map_size.width )
    
    def get_y_start_limit(self):
        if(self.position.y < 0):
            return 0
        
        return min(self.position.y,self.map_size.height )
    
    def get_x_end_limit(self):
        if(self.position.x + self.map_size.width < 0):
            return 0
        return self.get_width_limit_by_windows_size()

    def get_y_end_limit(self):
        if(self.position.y + self.map_size.height < 0):
            return 0
        return self.get_height_limit_by_windows_size()
    
    def get_positions_available(self):
        return [Position(tx,ty) for tx in xrange(self.x_start, self.x_end) for ty in xrange(self.y_start, self.y_end)]
                
    
    def get_width_limit_by_windows_size(self):
        size_by_window =  self.position.x + int(self.window_size.width/self.tile_size.width) + 1
        limit_by_map = self.map_size.width-1
        
        return min(size_by_window, limit_by_map)
    
    def get_height_limit_by_windows_size(self):
        size_by_window =  self.position.y + int(self.window_size.height/self.tile_size.height)
        limit_by_map = self.map_size.height-1
        
        return min(size_by_window, limit_by_map)
    
    