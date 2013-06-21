from viewport import Viewport 
from helpers import *
from cam import *
import renderer

class Scene(object):
    
    def __init__(self, filename, windows_width, window_height, sprites ):
        self.tmx_data = helpers.TmxDataProvider(filename)
        self.tile_size = self.tmx_data.get_tile_size()
        
        self.size = self.tmx_data.get_map_size()
        self.cam = Camera(Position(0,0))
        
        self.renderer = renderer.sfml_renderer(sprites)
        
        windows_size = Size(windows_width, window_height)
        viewport_limit = Limits(Position(0,0), self.size, windows_size, self.tile_size)
        self.viewport = Viewport(Position(0,0),  viewport_limit)
        
        self.visible_layers = []
        
    
    def set_visible_layers(self, layers):
        self.visible_layers = layers
        
    def render(self , context):
        for layer in self.visible_layers:
            self._render_from_layer(context, layer)
    
    def set_camera(self, camera):
        self.camera = camera
        
    def set_images_path(self, path):
        self.renderer.set_images_path(path)
        
    def _render_from_layer(self, context, layer):
        tmx_layer = self.tmx_data.get_layer(layer['name'])
        tmx_layer.set_distance(layer['distance'])
        self._render_layer(tmx_layer, context)


    def _render_layer(self, layer, context):
        layer_position = self._get_position_from_layer(layer)
        self.viewport.set_layer_position(layer_position, self.tile_size)
        for position in self.viewport.get_visibles_tiles():
            tile = self.tmx_data.get_tile(layer, position)
            self.renderer.render_tile(tile, layer_position , context)


    def _get_position_from_layer(self, layer):
        camera_position = self.cam.get_position()
        distance_factor = layer.get_distance_factor()
        return Position(camera_position.x * distance_factor , camera_position.y * distance_factor) 
        
    
    
    def update(self, dt):
        self.cam.update(dt)
        
