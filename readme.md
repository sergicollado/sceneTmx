# python-sfml  SceneTMX library
###v 0.8

## Synopsis
Simple library to render tiled tmx maps with python-sfm library.

## Dependencies
python library tmxlib
pip install tmxlib

## Code Example
```python
from character import Character
import scene
from scene.renderer import drawables

try:
    
    # first create a sprites pool
    sprites = drawables.Sprites()                                           
    
    #instance sceneTmx with size of window
    scene = scene.Scene(MAPS_PATH+"textMap.tmx", width, height, sprites)    
    #a string for setting the Path of your images
    scene.set_images_path(IMAGES_PATH)                                      
    	
    #set visible layers of scene with a list, 
    #distance key is a multiplier for the parallax layer displacement 
    layers = [{'name':'c1' , 'distance': 1}]
    scene.set_visible_layers(layers)              
    
except IOError: 
    print IOError
    exit(1)

```

## Motivation
Create a tool in order to make tiled based games with python-sfml.

## Installation
Insert scene package in your game folder structure, and import.

## License
CC BY
