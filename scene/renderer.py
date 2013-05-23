import sfml as sf
import drawables

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