import unittest
import sure

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../scene'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../scene/helpers'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from config import *
from scene import *
from helpers import *

class TestLimits(unittest.TestCase):

    def setUp(self):
        
        self.cam_position = Position(10,10)
        self.size_map = Size(100,100)
        self.size_window = Size(800,600)
        self.tile_size = Size(32,32)
        self.limits= Limits( self.cam_position, self.size_map , self.size_window , self.tile_size )
    
    def test_intialitation_limit(self):
        self.assertIsInstance(self.limits, Limits)
        
    
    def test_window_size_should_set_limit(self):
        x_limit = self.limits.get_x_end_limit()
        limit_by_window = int( self.size_window.width/self.tile_size.width ) + self.cam_position.x
        
        self.assertLess(x_limit,self.size_map.width )
        self.assertEqual(x_limit,limit_by_window )
    #def test_when_panning_should_change_position(self):
        #self.camera.speed.aceleration = 2
        #self.camera.panning_right()
        #self.camera.update()
        
        #self.assertEqual(self.position.x, 2 )
       
        #self.camera.panning_left()
        #self.camera.update()
        
        #self.assertEqual(self.position.x, 1 )
    
        #self.camera.panning_top()
        #self.camera.update()
    
        #self.assertEqual(self.position.y, 2 )
    

    
if __name__ == '__main__' :
    unittest.main(verbosity=2)
