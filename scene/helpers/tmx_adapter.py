import tmxlib
from helpers import  *

class TmxDataProvider:
    def __init__(self,filename):
        self.tmx = tmxlib.Map.open(filename)

    def get_map_size(self):
        return  Size(self.tmx.size[0],self.tmx.size[1])

    def get_tile_size(self):
        size = self.tmx.tile_size
        return  Size(size[0],size[1])
    
    def get_layer(self, layer):
        return Layer(layer, self.tmx)
    
    def get_tile(self, layer, position):
        tile = Tile(layer, position)
        return tile
    
class Layer:
    def __init__(self,layer_name, tmx):
        self.rawlayer = tmx.layers[layer_name]
        self.distance = 1
    def set_distance(self, distance):
        self.distance = distance
        
    def get_tile(self, position):
        return self.rawlayer[position.x, position.y]
    
    def get_distance_factor(self):
        return self.distance
        
class Tile:
    def __init__(self, layer, position):
        self.rawtile = layer.get_tile(position)
        
    def is_empty(self):
        if not self.rawtile.image:
            return True
        return False
    
    def get_size(self):
        size = self.rawtile.size
        return Size(size[0], size[1])
    
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