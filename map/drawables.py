import sfml as sf

class Sprites:
    def __init__(self):
        self.sprites_pool = {}
        
    def get_sprite(self, source):
        if not source  in self.sprites_pool:
            texture = sf.Texture.from_file(source)
            self.sprites_pool[source] = sf.Sprite(texture)
        
        return self.sprites_pool[source]