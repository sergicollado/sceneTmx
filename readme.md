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
    
    sprites = drawables.Sprites() 											
    # first create a sprites pool
    
    scene = scene.Scene(MAPS_PATH+"textMap.tmx", width, height, sprites) 	
    #instance sceneTmx with size of window
    scene.set_images_path(IMAGES_PATH)									 	
    #a string for setting the Path of your images
    	
    scene.set_visible_layers =  [{'name':'c1' , 'distance': 1}]				 
    #set visible layers of scene with a list, 
    #distance key is a multiplier for the parallax layer displacement 
    
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
