'''
Name: Eyl
Members: Alex Haban, Matthew Hall, Colin Bui, Roman Groenewold
email: habanaj@mail.uc.edu
Assignment: Final Project
Course: IS 4010
Semester/Year: Fall 2022
Brief Description: 
Citations:
Anything else that's relevant:
'''

import json

Eyl = ["7479",
       "28893",
       "8017",
       "42048",
       "20572",
       "42060",
       "27510",
       "6635",
       "28893",
       "8017"]
Location = ["builders",
            "omnivore",
            "camps",
            "thanksgivings",
            "harvests",
            "thaws",
            "mossy",
            "booklets",
            "omnivore",
            "camps"]

jsonFile = 'EncryptedGroupHints.json'
with open(jsonFile) as f:
    jsonData = json.load(f)
    
dictionaryFile = 'english.txt'
myFile = open(dictionaryFile, 'r')
inputData = myFile.read()
dictionaryList = inputData.split('\n')


for i in jsonData['Eyl']:
    print(dictionaryList[int(i)])
