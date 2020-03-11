# coding: utf-8 

import json

class API():

    choice_file = "choice.json"
    choices = []

    data_file = "user_data.json"
    user_data = []

    def __init__(self):
        super().__init__()
        __loadData()
        

    def __loadData(self):
        with open(choice_file, 'r') as f:
            choices = json.load(f)

        with open(data_file, 'r') as f:
            user_data = json.load(f)

    def saveData(self):
        with open(data_file, 'w') as f:
            json.dump(user_data, f)

        with open(choice_file, 'w') as f:
            json.dump(choices, f)
    
    #ROOM
    def addRoom(self, room):
        choices['rooms'].append(room)

    def setRoom(self, room):
        choices['rooms'].pop(room)
        choices['rooms'].append(room)

    def removeRoom(self, room):
        choices['rooms'].pop(room)

    def getRooms(self):
        return choices['rooms']

    def getRoom(self, room):
        return choices['rooms'][room]

    #COMPUTER
    def addComputer(self, computer):
        user_data['computers'].append(computer)

    def setComputer(self, computer):
        user_data['computers'].pop(computer)
        user_data['computers'].append(computer)

    def removeComputer(self, computer):
        user_data['computers'].pop(computer)

    #SOFTWARE
    

    #PLUGINS
