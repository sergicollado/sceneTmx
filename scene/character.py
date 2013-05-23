from helpers import *
import renderer

class Character:
    def __init__(self, filename, tilesize):
        self.position = Position(0,0)
        self.speed = Speed()
        self.renderer = renderer.SfmlCharacterRenderer( filename, tilesize)

    def render(self, context):
        self.renderer.render(context)
        
    def horizontal_aceleration(self):
        self.speed.horizontal_aceleration()
        
    def horizontal_deceleration(self):
        self.speed.horizontal_deceleration()
        
    def update(self):
        self.speed.update()
        self.position.x += int(self.speed.velocity.horizontal)
        self.renderer.set_position(self.position)
        
    def set_velocity (self, velocity):
        self.speed.aceleration = velocity