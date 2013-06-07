import sfml as sf
import drawables
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../scene/helpers'))
import helpers


class sfml_renderer:
    def __init__(self):
        self.sprites = drawables.Sprites()
        self.images_path = ''
        
    def render_tile(self, tile, position, context ): 
        if  tile.is_empty():
            return False
        
        sprite = self.sprites.get_sprite(self.images_path + tile.get_image_source())
        self.set_image_sprite_appropiate(sprite, tile.get_image_position(), tile.get_size())
        sprite.position = self.get_tile_position(tile, position)
        self.render_sprite(sprite, context)

    def set_image_sprite_appropiate(self, sprite, image_position, tile_size):
        sprite.texture_rectangle = sf.Rectangle( image_position, (tile_size.width, tile_size.height))
    
    def render_sprite(self, sprite, context):
        context.draw(sprite)
    
    def get_tile_position(self, tile, position):
        tile_position = tile.get_pixels_position()
        return ( tile_position.x - position.x , tile_position.y - position.y )

    def set_images_path(self, path):
        self.images_path = path
        

class SfmlCharacterRenderer:
    def __init__(self, filename, tile_size):
        self.sprites = drawables.Sprites()
        self.sprite = self.sprites.get_sprite(filename)
        self.tile_size = tile_size
        self.image_position = (0,0)
        self.set_image_sprite_appropiate()
        self.position = helpers.Position(0,0)
        self.sprite.position = (self.position.x, self.position.y) 
        
    def set_position(self, position):
        self.position = position
        self.sprite.position = (self.position.x, self.position.y) 
    
    def set_image_sprite_appropiate(self):
        self.sprite.texture_rectangle = sf.Rectangle( self.image_position, (self.tile_size.width, self.tile_size.height))
    
    def render(self, context):
        context.draw(self.sprite)


    def set_images_path(self, path):
        self.images_path = path