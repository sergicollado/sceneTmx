class Position:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    
    def set_position(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return 'x: '+ str(self.x) + ' y: '+ str(self.y)