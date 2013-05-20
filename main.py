import sfml as sf
import map
from config import *

# create the main window
window = sf.RenderWindow(sf.VideoMode(1020, 600), "pySFML Window")

try:
    texture = sf.Texture.from_file(IMAGES_PATH+"twilight-tiles.png")
    sprite = sf.Sprite(texture)
    
    map = map.Map(MAPS_PATH+"textMap.tmx")
    map.images_path = IMAGES_PATH

    
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

        if type(event) is sf.KeyEvent and event.code is sf.Keyboard.RIGHT:
            map.cam.panning_right()
        if type(event) is sf.KeyEvent and event.code is sf.Keyboard.LEFT:
            map.cam.panning_left()
        if type(event) is sf.KeyEvent and event.code is sf.Keyboard.UP:
            map.cam.panning_top()
        if type(event) is sf.KeyEvent and event.code is sf.Keyboard.DOWN:
            map.cam.panning_down()
   
    window.clear() # clear screen
    map.update()
    map.render_from_layer(window,'c2')
    map.render_from_layer(window,'collisions')
    window.display() # update the window
