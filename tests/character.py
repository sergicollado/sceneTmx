import unittest

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../scene'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../renderer'))

from config import *
from scene import *

class TestCharacter(unittest.TestCase):

    def setUp(self):
        self.character = Character( IMAGES_PATH+"mikeypebalz.png",Size(57,101))
    
    def test_intialitation_camera(self):
        self.assertIsInstance(self.character, Character)
        
    def test_when_panning_should_change_position(self):
        velocity = 4
        self.character.set_velocity(velocity);
        self.character.horizontal_aceleration()
        self.character.update()
        self.assertLess(self.character.position.x, velocity )
        self.assertGreater(self.character.position.x, 0 )
     

    
if __name__ == '__main__' :
    unittest.main(verbosity=2)
