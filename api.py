# coding: utf-8 

import json, uuid

class API():

    choice_file = "choice.json"
    choices = []

    data_file = "user_data.json"
    user_data = []

    def __init__(self):
        super().__init__()
        self.__loadData()
        

    def __loadData(self):
        with open(self.choice_file, 'r') as f:
            self.choices = json.load(f)

        with open(self.data_file, 'r') as f:
            self.user_data = json.load(f)

    def saveData(self):
        with open(self.data_file, 'w') as f:
            json.dump(self.user_data, f)

        with open(self.choice_file, 'w') as f:
            json.dump(self.choices, f)
    
    #ROOM
    def addRoom(self, room):
        self.choices['rooms'][uuid.uuid1()] = room

    def setRoom(self, id, room):
        self.choices['rooms'][id] = room

    def removeRoom(self, id):
        self.choices['rooms'].remove(id)

    def getRooms(self):
        return self.choices['rooms']

    def getRoom(self, id):
        return self.choices['rooms'][id]

    #COMPUTER
    def addComputer(self, computer):
        self.user_data[uuid.uuid1()] = computer

    def setComputer(self, id, computer):
        self.user_data[id] = computer

    def removeComputer(self, id):
        self.user_data.remove(id)

    def getComputers(self):
        return self.user_data

    def getComputer(self, id):
        return self.user_data[id]

    #SOFTWARE
    def addSoftware(self, computer_id, software):
        self.user_data[computer_id]['softwares'][uuid.uuid1()] = software

    def setSoftware(self, computer_id, software_id, software):
        self.user_data[computer_id]['softwares'][software_id] = software

    def removeSoftware(self, computer_id, software_id):
        self.user_data[computer_id]['softwares'].remove(software_id)

    def getSoftwares(self, computer_id):
        return self.user_data[computer_id]['softwares']

    def getSoftware(self, computer_id, software_id):
        return self.user_data[computer_id]['softwares'][software_id]

    #PLUGINS
    def addPlugin(self, computer_id, software_id, plugin):
        self.user_data[computer_id]['softwares'][software_id]['add_on'][uuid.uuid1()] = plugin

    def setPlugin(self, computer_id, software_id, plugin_id, plugin):
        self.user_data[computer_id]['softwares'][software_id]['add_on'][plugin_id] = plugin

    def removePlugin(self, computer_id, software_id, plugin_id):
        self.user_data[computer_id]['softwares'][software_id]['add_on'].remove(plugin_id)

    def getPlugins(self, computer_id, software_id):
        return self.user_data[computer_id]['softwares'][software_id]['add-on']

    def getPlugin(self, computer_id, software_id, plugin_id):
        return self.user_data[computer_id]['softwares'][software_id]['add-on'][plugin_id]