import tmxlib
import sfml as sf
import viewport 

class Map(object):
    
    def __init__(self, filename ):
        self.tmx = tmxlib.Map.open(filename)
        self.tile_size = self.tmx.tile_size
        self.sprites = {}
        self.viewport = viewport.Viewport()
        self.viewport.x_end = self.tmx.size[0]
        self.viewport.y_end = self.tmx.size[1]
        self.images_path = ''
    
    def render(self, context):
        layer = self.tmx.layers['c2']
        self.render_layer(layer, context)


    def render_layer(self, layer, context):
        for tx in xrange(self.viewport.x_start, self.viewport.x_end):
            for ty in xrange(self.viewport.y_start, self.viewport.y_end):
                tile = layer[tx,ty]
                self.render_tile(tile, context)


    def render_tile(self, tile, context ): 
        if not tile.image:
            return False
            
        tile_image_position = tile.image.top_left
        pixel_position = self.tile_position_to_pixels(tile.pos , self.tile_size)
        sprite = self.get_sprite(tile.image.image.source)

        self.set_image_sprite_appropiate(sprite, tile_image_position)
        sprite.position = pixel_position
        self.render_sprite(sprite, context)

    def set_image_sprite_appropiate(self, sprite, image_position):
        sprite.texture_rectangle = sf.Rectangle( image_position, self.tile_size)
    
    def get_sprite(self, source):
        if not source  in self.sprites:
            texture = sf.Texture.from_file(self.images_path + source)
            self.sprites[source] = sf.Sprite(texture)
        
        return self.sprites[source]
        
    def render_sprite(self, sprite, context):
        context.draw(sprite)
    
    def tile_position_to_pixels(self, position, tile_size):
        return (position[0] * tile_size[0] , position[1] * tile_size[1] )
    
    

