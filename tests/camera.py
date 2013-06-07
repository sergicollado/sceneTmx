import unittest
import sure

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../scene'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../scene/helpers'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from config import *
from scene import *

class TestCamera(unittest.TestCase):

    def setUp(self):
        self.position= helpers.Position()
        self.camera = scene.Camera(self.position)
    
    def test_intialitation_camera(self):
        self.assertIsInstance(self.camera, Camera)
        
    def test_when_panning_should_change_position(self):
        self.camera.speed.aceleration = 2
        self.camera.panning_right()
        self.camera.update()
        
        self.assertEqual(self.position.x, 2 )
       
        self.camera.panning_left()
        self.camera.panning_left()
        self.camera.update()
        
        self.assertEqual(self.position.x, 0 )
    
        self.camera.panning_top()
        self.camera.update()
    
        self.assertEqual(self.position.y, -2 )
    

    
if __name__ == '__main__' :
    unittest.main(verbosity=2)
