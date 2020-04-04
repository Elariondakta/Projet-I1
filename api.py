# coding: utf-8 

import json, uuid
import logging
class API():

    choice_file = "./data/choice.json"
    choices = []

    data_file = "./data/user_data.json"
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
        try:
            with open(self.data_file, 'w') as f:
                json.dump(self.user_data, f)

            with open(self.choice_file, 'w') as f:
                json.dump(self.choices, f)
        except BaseException:
            return False
        return True

    # ROOM
    def addRoom(self, room, building):
        self.choices['rooms'][str(uuid.uuid4())] = {
            "building_name": building,
            "room_name": room
        }
        return self.saveData()

    """
    Renomme une salle avec commme arguments un id et le nouveau nom
    """
    def renameRoom(self, id, name):
        self.choices['rooms'][id]["room_name"] = name
        return self.saveData()
 
    def removeRoom(self, id):
        del self.choices['rooms'][id]
        return self.saveData()

    def getRooms(self):
        return self.choices['rooms']

    def getRoom(self, id):
        return self.choices['rooms'][id]
    """
    Retourne une liste de tous les bâtiments disponibles
    """
    def getBuildings(self):
        results = {}
        for room_id in self.choices["rooms"].keys():
            if self.choices["rooms"][room_id]["building_name"] in results.values():
                results[room_id] = self.choices["rooms"][room_id]["building_name"]
        return results

    """
    Recherche d'une salle parmi la liste de toutes les salles disponibles
    """
    def searchRooms(self, query):
        results = {}
        for room_id in self.choices["rooms"].keys():
            if self.choices["rooms"][room_id]["room_name"].find(query) != -1:
                results[room_id] = self.choices["rooms"][room_id]
        return results

    #COMPUTER
    def addComputer(self, computer):
        self.user_data[str(uuid.uuid4())] = computer

    def setComputer(self, id, computer):
        self.user_data[id] = computer

    def removeComputer(self, id):
        self.user_data.remove(id)

    def getComputers(self):
        return self.user_data

    def getComputer(self, id):
        return self.user_data[id]

    """
    Permet de trouver tous les ordinateurs dans une salle
    Renvoie un Dictionnaire avec les infos pour chaque ordinateur et son id comme clef
    """ 
    def getComputersInRoom(self, roomId):
        results = {}
        for computer_key in list(self.user_data.keys()):
            if self.user_data[computer_key]["localisation"]["room_id"] == roomId:
                results[computer_key] = self.user_data[computer_key]
        return results

    #SOFTWARE
    def addSoftware(self, computer_id, software):
        self.user_data[computer_id]['softwares'][str(uuid.uuid4())] = software

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
        self.user_data[computer_id]['softwares'][software_id]['add_on'][str(uuid.uuid4())] = plugin

    def setPlugin(self, computer_id, software_id, plugin_id, plugin):
        self.user_data[computer_id]['softwares'][software_id]['add_on'][plugin_id] = plugin

    def removePlugin(self, computer_id, software_id, plugin_id):
        self.user_data[computer_id]['softwares'][software_id]['add_on'].remove(plugin_id)

    def getPlugins(self, computer_id, software_id):
        return self.user_data[computer_id]['softwares'][software_id]['add-on']

    def getPlugin(self, computer_id, software_id, plugin_id):
        return self.user_data[computer_id]['softwares'][software_id]['add-on'][plugin_id]