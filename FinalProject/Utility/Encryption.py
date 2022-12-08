'''
Name: Eyl
Members: Alex Haban, Matthew Hall, Colin Bui, Roman Groenewold
email: habanaj@mail.uc.edu, hall4mj@mail.uc.edu, groenern@mail.uc.edu, buici@mail.uc.edu
Assignment: Final Project
Course: IS 4010
Semester/Year: Fall 2022
Brief Description: This is our Final Project for Advanced Application Development
Citations:
Anything else that's relevant:
'''
import json

def getEncryptedData():
    jsonFile = 'EncryptedGroupHints.json'
    with open(jsonFile) as f:
        jsonData = json.load(f)
        
    dictionaryFile = 'english.txt'
    myFile = open(dictionaryFile, 'r')
    inputData = myFile.read()
    dictionaryList = inputData.split('\n')
    
    encryptedMessage = []
    for i in jsonData['Eyl']:
        encryptedMessage.append(dictionaryList[int(i)])
       
    return encryptedMessage