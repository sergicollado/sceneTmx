import sfml as sf
from scene import *
from config import *
from scene.helpers import *

# create the main window
width = 1020
height = 600
window = sf.RenderWindow(sf.VideoMode(1020, 600), "pySFML Window")
window.framerate_limit = 60
window.vertical_synchronization = True

try:
    texture = sf.Texture.from_file(IMAGES_PATH+"twilight-tiles.png")
    sprite = sf.Sprite(texture)
    
    scene = Scene(MAPS_PATH+"textMap.tmx", Size(width, height))
    scene.set_images_path(IMAGES_PATH)
    
except IOError: 
    print IOError
    exit(1)




# start the game loop
while window.is_open:
    # process events
    for event in window.events:
      # close window: exit
        if type(event) is sf.CloseEvent or type(event) is sf.KeyEvent and event.code is sf.Keyboard.ESCAPE:
            window.close()

        if type(event) is sf.KeyEvent and event.code is sf.Keyboard.RIGHT:
            scene.cam.panning_right()
        if type(event) is sf.KeyEvent and event.code is sf.Keyboard.LEFT:
            scene.cam.panning_left()
        if type(event) is sf.KeyEvent and event.code is sf.Keyboard.UP:
            scene.cam.panning_top()
        if type(event) is sf.KeyEvent and event.code is sf.Keyboard.DOWN:
            scene.cam.panning_down()
   
    window.clear() # clear screen
    scene.update()
    scene.render_from_layer(window,'c2')
    scene.render_from_layer(window,'collisions')
    window.display() # update the window
