import tmxlib
from helpers import  *

class TmxDataProvider:
    def __init__(self,filename):
        self.tmx = tmxlib.Map.open(filename)

    def get_map_size(self):
        return  self.tmx.size

    def get_tile_size(self):
        size = self.tmx.tile_size
        return  Size(size[0],size[1])
    
    def get_layer(self, layer):
        return self.tmx.layers[layer]
    
    def get_tile(self, layer, position):
        tile = Tile(layer, position)
        return tile
    
class Tile:
    def __init__(self, layer, position):
        self.rawtile = layer[position.x, position.y]
        
    def is_empty(self):
        if not self.rawtile.image:
            return True
        return False
    
    def get_image_position(self):
        return self.rawtile.image.top_left
    
    def get_position(self):
        return self.rawtile.pos
    
    def get_tile_image_position(self):
        return self.rawtile.image.top_left
    
    def get_image_source(self):
        return self.rawtile.image.image.source
    
    def get_pixels_position(self):
        return Position(self.rawtile.pos[0] * self.rawtile.size[0] , self.rawtile.pos[1] * self.rawtile.size[1] )