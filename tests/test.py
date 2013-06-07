import unittest
import sure

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../scene'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../scene/helpers'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from config import *
from scene import *

class TesTing(unittest.TestCase):

    def setUp(self):
        self.scene = Scene(MAPS_PATH+"textMap.tmx", Size(800, 600))
        self.scene.images_path = IMAGES_PATH
    
    def test_entorno(self):
        (4).should.be.equal(2 + 2)
        (5).should.be.greater_than(4)

    def test_intialitation_scenario(self):
        self.assertIsInstance(self.scene, Scene)
        

class TestVelocity(unittest.TestCase):
    
    def setUp(self):
        self.speed = helpers.Speed()
        
        
    def tearDown(self):
        self.speed.velocity.vertical = self.speed.velocity.horizontal = 0
        
    def test_when_acelerate(self):
        self.speed.vertical_aceleration()
        (self.speed.velocity.vertical).should.be.equal(self.speed.aceleration)
        
        self.speed.horizontal_aceleration()
        (self.speed.velocity.horizontal).should.be.equal(self.speed.aceleration)
        
    def test_when_decelerate(self):
        self.speed.horizontal_deceleration()
        (self.speed.velocity.horizontal).should.be.equal(-self.speed.aceleration)
        
        self.speed.vertical_deceleration()
        (self.speed.velocity.vertical).should.be.equal(-self.speed.aceleration)

    def test_speed_reduction(self):
        self.speed.vertical_aceleration()
        self.speed.reduce_vertical_speed()
        (self.speed.velocity.vertical).should.be.lower_than(self.speed.aceleration)
        self.speed.reduce_horizontal_speed()
        (self.speed.velocity.horizontal).should.be.lower_than(self.speed.aceleration)
    
    
    
if __name__ == '__main__' :
    unittest.main(verbosity=2)
