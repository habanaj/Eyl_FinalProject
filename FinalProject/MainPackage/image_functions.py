'''
Created on Dec 6, 2022

@author: Matthew Hall
'''
from PIL import Image, ImageFilter, ImageDraw, ImageFont
import os, sys
#import requests
from io import BytesIO

def load_image( filename ) :
    try:
        myimage = Image.open(filename)
        myimage.load()
        return myimage
    except:
        return None #This is all we can do at this point. This won't crash here now