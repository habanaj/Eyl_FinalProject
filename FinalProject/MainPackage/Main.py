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
import json

# This one is in Main.py only imports from the image_Functions module
from Utility import image_functions, Encryption

if __name__=="__main__":
    print(Encryption.getEncryptedData())
    image_functions.loadImage("OurTeam.jpeg")
    
    
