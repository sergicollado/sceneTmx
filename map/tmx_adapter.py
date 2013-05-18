import tmxlib

class TmxDataProvider:
    def __init__(self,filename):
        self.tmx = tmxlib.Map.open(filename)

    def get_tile_size(self):
        return  self.tmx.tile_size
    
    def get_layer(self, layer):
        return self.tmx.layers[layer]
    
    def get_tile(self, layer, position):
        return layer[position.x, position.y]