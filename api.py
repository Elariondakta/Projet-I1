# coding: utf-8 

import json, uuid

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
        choices['rooms'][uuid.uuid1()] = room

    def setRoom(self, id, room):
        choices['rooms'][id] = room

    def removeRoom(self, id):
        choices['rooms'].remove(id)

    def getRooms(self):
        return choices['rooms']

    def getRoom(self, id):
        return choices['rooms'][id]

    #COMPUTER
    def addComputer(self, computer):
        user_data[uuid.uuid1()] = computer

    def setComputer(self, id, computer):
        user_data[id] = computer

    def removeComputer(self, id):
        user_data.remove(id)

    def getComputers(self):
        return user_data

    def getComputer(self, id):
        return user_data[id]

    #SOFTWARE
    def addSoftware(self, computer_id, software):
        user_data[computer_id]['softwares'][uuid.uuid1()] = software

    def setSoftware(self, computer_id, software_id, software):
        user_data[computer_id]['softwares'][software_id] = software

    def removeSoftware(self, computer_id, software_id):
        user_data[computer_id]['softwares'].remove(software_id)

    def getSoftwares(self, computer_id):
        return user_data[computer_id]['softwares']

    def getSoftware(self, computer_id, software_id):
        return user_data[computer_id]['softwares'][software_id]

    #PLUGINS
    def addPlugin(self, computer_id, software_id, plugin):
        user_data[computer_id]['softwares'][software_id]['add_on'][uuid.uuid1()] = plugin

    def setPlugin(self, computer_id, software_id, plugin_id, plugin):
        user_data[computer_id]['softwares'][software_id]['add_on'][plugin_id] = plugin

    def removePlugin(self, computer_id, software_id, plugin_id):
        user_data[computer_id]['softwares'][software_id]['add_on'].remove(plugin_id)

    def getPlugins(self, computer_id, software_id):
        return user_data[computer_id]['softwares'][software_id]['add-on']

    def getPlugin(self, computer_id, software_id, plugin_id):
        return user_data[computer_id]['softwares'][software_id]['add-on'][plugin_id]