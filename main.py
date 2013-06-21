import sfml as sf
from scene import *
from config import *
from scene.renderer import drawables

# create the main window
width = 800
height = 600
window = sf.RenderWindow(sf.VideoMode(width, height), "pySFML Window")
window.framerate_limit = 60
window.vertical_synchronization = True

try:
    texture = sf.Texture.from_file(IMAGES_PATH+"twilight-tiles.png")
    
    sprites = drawables.Sprites()
    scene = Scene(MAPS_PATH+"textMap.tmx", width, height, sprites)
    scene.set_images_path(IMAGES_PATH)
    layers = [
        {'name':'c2' , 'distance': 0.8},
        {'name':'c1' , 'distance': 1},
    ]
    scene.set_visible_layers(layers)

    
    player = Character(IMAGES_PATH+"mikeypebalz.png", 57,101, sprites)
    
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
            player.horizontal_aceleration()
        if type(event) is sf.KeyEvent and event.code is sf.Keyboard.LEFT:
            scene.cam.panning_left()
            player.horizontal_deceleration()
        if type(event) is sf.KeyEvent and event.code is sf.Keyboard.UP:
            scene.cam.panning_top()
        if type(event) is sf.KeyEvent and event.code is sf.Keyboard.DOWN:
            scene.cam.panning_down()
   
    window.clear() # clear screen
    scene.update()
    scene.render(window)
    player.update()
    player.render(window)
    window.display() # update the window
