import helpers
import math 

class Viewport(object):
    def __init__(self, position  , size ):
        self.position = position
        self.size = size
        self.limits = helpers.Limits(position, size)        
        
    def set_pixels_position(self,position, tile_size):
        self.set_position_from_pixels(position, tile_size)
        self.limits.set_position(position)
        

    def get_tile_position_from_pixels(self, coordinate, tile_size, max_tilesize):
        if( coordinate < 0):
            return 0
        tile_position = int(math.floor(coordinate/tile_size))

        return min(tile_position, max_tilesize-1)
    
    def set_position_from_pixels(self, position, tile_size):
        self.position.x =  self.get_tile_position_from_pixels(position.x, tile_size.width , self.size.width)
        self.position.y = self.get_tile_position_from_pixels(position.y, tile_size.height, self.size.height)
        