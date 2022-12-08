'''
Name: Eyl
Members: Alex Haban, Matthew Hall, Colin Bui, Roman Groenewold
email: habanaj@mail.uc.edu, hall4mj@mail.uc.edu, groenern@mail.uc.edu, buici@mail.uc.edu
Assignment: Final Project
Course: IS 4010
Semester/Year: Fall 2022
Brief Description: 
Citations:
Anything else that's relevant:
'''
from PIL import Image

def loadImage(fileName) :
    try:
        myImage = Image.open(fileName)
        myImage.show()        
    except:
        return None #This is all we can do at this point. This won't crash here now
