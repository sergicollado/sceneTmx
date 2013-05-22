import tmx_adapter 
from viewport import Viewport 
from helpers import *
import drawables
from cam import *
import renderer

class Scene(object):
    
    def __init__(self, filename, windows_size ):
        self.tmx_data = tmx_adapter.TmxDataProvider(filename)
        self.tile_size = self.tmx_data.get_tile_size()
        
        self.size = self.tmx_data.get_map_size()
        self.cam = Camera(Position(0,0))
        
        self.renderer = renderer.sfml_renderer()
        
        viewport_limit = Limits(Position(0,0), self.size, windows_size, self.tile_size)
        self.viewport = Viewport(Position(0,0),  viewport_limit)
    
    def set_camera(self, camera):
        self.camera = camera
        
    def set_images_path(self, path):
        self.renderer.set_images_path(path)
        
    def render_from_layer(self, context, layer_name):
        layer = self.tmx_data.get_layer(layer_name)
        self.render_layer(layer, context)


    def render_layer(self, layer, context):
        for position in self.viewport.get_visibles_tiles():
                tile = self.tmx_data.get_tile(layer, position)
                self.renderer.render_tile(tile, self.cam.get_position(), context)


    def update(self):
        self.cam.update()
        self.viewport.set_cam_position(self.cam.get_position(), self.tile_size)