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