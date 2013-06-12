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
        self.scene = Scene(MAPS_PATH+"textMap.tmx", 800, 600)
        self.scene.images_path = IMAGES_PATH
    
    def test_entorno(self):
        (4).should.be.equal(2 + 2)
        (5).should.be.greater_than(4)

    def test_intialitation_scenario(self):
        self.assertIsInstance(self.scene, Scene)
        

class TestVelocity(unittest.TestCase):
    
    def setUp(self):
        self.physical_object = helpers.PhysicalObject()
        
        
    def tearDown(self):
        self.physical_object.velocity.vertical = self.physical_object.velocity.horizontal = 0
        
    def test_when_acelerate(self):
        self.physical_object.vertical_aceleration()
        (self.physical_object.velocity.vertical).should.be.equal(self.physical_object.aceleration)
        
        self.physical_object.horizontal_aceleration()
        (self.physical_object.velocity.horizontal).should.be.equal(self.physical_object.aceleration)
        
    def test_when_decelerate(self):
        self.physical_object.horizontal_deceleration()
        (self.physical_object.velocity.horizontal).should.be.equal(-self.physical_object.aceleration)
        
        self.physical_object.vertical_deceleration()
        (self.physical_object.velocity.vertical).should.be.equal(-self.physical_object.aceleration)

    
    
    
if __name__ == '__main__' :
    unittest.main(verbosity=2)
