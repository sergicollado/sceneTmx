from helpers import *
import renderer

class Character:
    def __init__(self, filename, tile_width, tile_height, sprites):
        self.position = Position(0,0)
        self.physical_object = PhysicalObject()
        tilesize = Size(tile_width, tile_height)
        self.renderer = renderer.SfmlCharacterRenderer( filename, tilesize, sprites)

    def render(self, context):
        self.renderer.render(context)
        
    def horizontal_aceleration(self):
        self.physical_object.horizontal_aceleration()
        
    def horizontal_deceleration(self):
        self.physical_object.horizontal_deceleration()
        
    def update(self):
        self.physical_object.update()
        self.position.x += int(self.physical_object.velocity.horizontal)
        self.renderer.set_position(self.position)
        
    def set_velocity (self, velocity):
        self.physical_object.aceleration = velocity