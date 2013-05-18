import tmx_adapter 
import sfml as sf
import viewport 
import data_types
import drawables
from cam import *


class Map(object):
    
    def __init__(self, filename ):
        self.tmx_data = tmx_adapter.TmxDataProvider(filename)
        self.tile_size = self.tmx_data.get_tile_size()
        self.size = self.tmx_data.get_map_size()
        self.sprites = drawables.Sprites()
        self.cam = Camara(data_types.Position(0,0))
        
        size = data_types.Size(self.size[0], self.size[1])
        self.viewport = viewport.Viewport(self.cam.get_position(), size )
        self.images_path = ''
    
    def render(self, context):
        layer = self.tmx_data.get_layer('c2')
        self.render_layer(layer, context)


    def render_layer(self, layer, context):
        for tx in xrange(self.viewport.limits.x_start, self.viewport.limits.x_end):
            for ty in xrange(self.viewport.limits.y_start, self.viewport.limits.y_end):
                position  = data_types.Position(tx,ty)
                tile = self.tmx_data.get_tile(layer, position)
                self.render_tile(tile, context)

    def render_tile(self, tile, context ): 
        if  tile.is_empty():
            return False
        
        sprite = self.sprites.get_sprite(self.images_path + tile.get_image_source())
        self.set_image_sprite_appropiate(sprite, tile.get_image_position())
        sprite.position = self.get_tile_position(tile)
        self.render_sprite(sprite, context)

    def set_image_sprite_appropiate(self, sprite, image_position):
        sprite.texture_rectangle = sf.Rectangle( image_position, self.tile_size)
    
        
    def render_sprite(self, sprite, context):
        context.draw(sprite)
    
    def tile_position_to_pixels(self, position, tile_size):
        return (position[0] * tile_size[0] , position[1] * tile_size[1] )
    
    def get_tile_position(self, tile):
        tile_position = tile.get_pixels_position()
        return ( tile_position[0] - self.cam.x , tile_position[1] - self.cam.y )

    def update(self):
        self.cam.update()
