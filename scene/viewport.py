import helpers
import math 
import copy

class Viewport(object):
    def __init__(self, position  , limits ):
        self.position = position
        self.limits = limits    
        
    def set_layer_position(self,position, tile_size):
        cam_position = helpers.Position(position.x,position.y)
        self.set_position_from_pixels(cam_position, tile_size)
        self.limits.set_position(copy.copy(self.position))
        

    def get_tile_position_from_pixels(self, coordinate, tile_size, max_tilesize):
        if( coordinate < 0):
            return 0
        tile_position = int(math.floor(coordinate/tile_size))

        return min(tile_position, max_tilesize-1)
    
    def set_position_from_pixels(self, position, tile_size):
        self.position.x =  int(math.floor(position.x/tile_size.width))
        self.position.y = int(math.floor(position.y/tile_size.height))
        
    def get_visibles_tiles(self):
        return self.limits.get_positions_available()