import sfml as sf

import scene
import character
from config import *
from scene.renderer import drawables

# create the main window
width = 1280
height = 820
window = sf.RenderWindow(sf.VideoMode(width, height), "pySFML Window")
window.framerate_limit = 60
window.vertical_synchronization = True

pressed_button_right = False
pressed_button_left = False
pressed_button_top = False
pressed_button_down = False
clock = sf.Clock()


try:
    texture = sf.Texture.from_file(IMAGES_PATH+"twilight-tiles.png")
    
    sprites = drawables.Sprites()
    scene = scene.Scene(MAPS_PATH+"textMap.tmx", width, height, sprites)
    scene.set_images_path(IMAGES_PATH)
    layers = [
        {'name':'c2' , 'distance': 0.8},
        {'name':'c1' , 'distance': 1},
    ]
    scene.set_visible_layers(layers)

    
    player = character.Character(IMAGES_PATH+"mikeypebalz.png", 57,101, sprites)
    player.set_velocity(10)
except IOError: 
    print IOError
    exit(1)




# start the game loop
while window.is_open:
    # process events
    for event in window.events:
      # close window: exit
        if type(event) is sf.CloseEvent or sf.Keyboard.is_key_pressed(sf.Keyboard.ESCAPE):
            window.close()

        if sf.Keyboard.is_key_pressed(sf.Keyboard.RIGHT):
            pressed_button_right = True
        else:
            pressed_button_right = False

        if sf.Keyboard.is_key_pressed(sf.Keyboard.LEFT):
            pressed_button_left = True
        else:
            pressed_button_left = False

        if sf.Keyboard.is_key_pressed(sf.Keyboard.UP):
            pressed_button_top = True
        else:
            pressed_button_top = False

        if sf.Keyboard.is_key_pressed(sf.Keyboard.DOWN):
            pressed_button_down = True
        else:
            pressed_button_down = False
    
    if(pressed_button_right):
        scene.cam.panning_right()
        player.horizontal_aceleration() 
    if(pressed_button_left):
        scene.cam.panning_left()
        player.horizontal_deceleration() 
    if(pressed_button_top):
        scene.cam.panning_top()
    if(pressed_button_down):
        scene.cam.panning_down()

    time  = clock.restart().seconds*10
    window.clear() 
    scene.update(time)
    scene.render(window)
    player.update(time)
    player.render(window)
    window.display() 