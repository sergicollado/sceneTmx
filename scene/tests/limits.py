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
        limit_by_window = int( self.size_window.width/self.tile_size.width ) + self.cam_position.x+1
        
        self.assertLess(x_limit,self.size_map.width )
        self.assertEqual(x_limit,limit_by_window )
        
    def test_start_limit_when_is_out_in_negative_position(self):
        out_range_position = Position(-100,-100)
        limits= Limits( out_range_position, self.size_map , self.size_window , self.tile_size )
    
        x_start_limit = limits.get_x_start_limit()
        self.assertEqual(x_start_limit, 0)

        y_start_limit = limits.get_y_start_limit()
        self.assertEqual(y_start_limit, 0)
        
    def test_start_limit_when_is_out_in_positive_position(self):
        out_range_position = Position(+100,+100)
        limits= Limits( out_range_position, self.size_map , self.size_window , self.tile_size )
    
        x_start_limit = limits.get_x_start_limit()
        self.assertEqual(x_start_limit, 100)

        y_start_limit = limits.get_y_start_limit()
        self.assertEqual(y_start_limit, 100)
        
    def test_end_limit_when_is_out_of_range(self):
        out_range_position = Position(100,100)
        limits= Limits( out_range_position, self.size_map , self.size_window , self.tile_size )
    
        x_start_limit = limits.get_x_end_limit()
        self.assertEqual(x_start_limit, 99)

        y_start_limit = limits.get_y_end_limit()
        self.assertEqual(y_start_limit, 99)
        

    
if __name__ == '__main__' :
    unittest.main(verbosity=2)
