import sfml as sf
import map
from config import *

# create the main window
window = sf.RenderWindow(sf.VideoMode(1020, 600), "pySFML Window")

try:
    # load a sprite to display
    print ROOT_PATH
    print ASSETS_PATH
    print IMAGES_PATH+"twilight-tiles.png"
    texture = sf.Texture.from_file(IMAGES_PATH+"twilight-tiles.png")
    sprite = sf.Sprite(texture)
    
    map = map.Map(MAPS_PATH+"textMap.tmx")
    map.images_path = IMAGES_PATH
    map.viewport.x_end = 50
    #map.viewport.y_end = 5
    
    #map.render_sprite(sprite,window)
    
except IOError: 
    print IOError
    exit(1)




# start the game loop
while window.is_open:
    # process events
    for event in window.events:
      # close window: exit
      if type(event) is sf.CloseEvent:
         window.close()

    

   
    window.clear() # clear screen
    map.render(window)
    window.display() # update the window
