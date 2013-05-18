from map import *
import unittest
import sure

class TesTing(unittest.TestCase):
	
	def setUp(self):
		self.mapa = Map("textMap.tmx")
		
	def test_entorno(self):
		(4).should.be.equal(2 + 2)
		(5).should.be.greater_than(4)

	def test_intialitation_map(self):
		(self.mapa).should.be.an('map.Map')


	#map = 

	#print (map).should.be.an('map.Map')

	#map.render() 


if __name__ == '__main__' :
	unittest.main(verbosity=2)
