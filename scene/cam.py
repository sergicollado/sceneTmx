import helpers

class Camera:
    def __init__(self, position):
        self.position = position
        self.physical_object = helpers.PhysicalObject()
        
    def get_position(self):
        return self.position
    
    def panning_right(self):
        self.physical_object.horizontal_aceleration()
        
    def panning_left(self):
        self.physical_object.horizontal_deceleration()

    def panning_top(self):
        self.physical_object.vertical_deceleration() 

    def panning_down(self):
        self.physical_object.vertical_aceleration()
        
    def set_position(self, position):
        self.position = position
        self.physical_object.reset()
        
    def update(self):
        self.position.x += int(self.physical_object.velocity.horizontal)
        self.position.y += int(self.physical_object.velocity.vertical)
        self.physical_object.update()

    
    def __str__(self):
        return 'position: '+ str(self.position.x)+',' +str(self.position.y)+' physical_object: '+ str(self.physical_object.velocity.horizontal)+','+str(self.physical_object.velocity.vertical) 