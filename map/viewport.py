import data_types
import math 

class Viewport(object):
    def __init__(self, position  , size ):
        self.position = position
        self.size = size
        self.limits = data_types.Limits((self.position.x,self.get_xend_limit(),self.position.y ,self.get_yend_limit()))
        
    def set_size(self, width, height):
        self.size = size
        
        
    def set_pixels_position(self, x, y , tile_size):
        self.position.x =  self.get_tile_position_from_pixels(x, tile_size.width , self.size.width)
        self.position.y = self.get_tile_position_from_pixels(y, tile_size.height, self.size.height)
        self.limits.set_limits((self.position.x,self.get_xend_limit(),self.position.y ,self.get_xend_limit()))
        

    def get_xend_limit(self):
        return min(self.position.x + self.size.width, self.size.width-1)

    def get_yend_limit(self):
        return min(self.position.x + self.size.width, self.size.height-1)
        
    def get_tile_position_from_pixels(self, coordenate, tile_size, max_tilesize):
        if( coordenate < 0):
            return 0
        tile_position = int(math.floor(coordenate/tile_size))
        
        return min(tile_position, max_tilesize-1)