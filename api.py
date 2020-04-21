# coding: utf-8 

import json, uuid
import logging
class API():

    choice_file = "./data/choice.json"

    computer_file = "./data/computers.json"

    room_file = "./data/rooms.json"

    @staticmethod 
    def loadData():
        with open(API.choice_file, 'r') as f:
            API.choice_data = json.load(f)

        with open(API.computer_file, 'r') as f:
            API.computer_data = json.load(f)
        
        with open(API.room_file, 'r') as f:
            API.room_data = json.load(f)

    @staticmethod 
    def saveData():
        try:
            with open(API.computer_file, 'w') as f:
                json.dump(API.computer_data, f)

            with open(API.room_file, 'w') as f:
                json.dump(API.room_data, f)
        except BaseException:
            return False
        return True

    # ROOM
    @staticmethod 
    def addRoom(room, building):
        API.room_data[str(uuid.uuid4())] = {
            "building_name": building,
            "room_name": room
        }
        return API.saveData()

    """
    Renomme une salle avec commme arguments un id et le nouveau nom
    """
    @staticmethod 
    def renameRoom(id, name):
        API.room_data[id]["room_name"] = name
        return API.saveData()
 
    @staticmethod 
    def removeRoom(id):
        del API.room_data[id]
        return API.saveData()

    @staticmethod 
    def getRooms():
        return API.room_data

    @staticmethod 
    def getRoom(id):
        return API.room_data[id]
    """
    Retourne une liste de tous les bâtiments disponibles
    """
    @staticmethod 
    def getBuildings():
        results = {}
        for room_id in API.room_data.keys():
            if API.room_data[room_id]["building_name"] in results.values():
                results[room_id] = API.room_data[room_id]["building_name"]
        return results

    """
    Recherche d'une salle parmi la liste de toutes les salles disponibles
    """
    @staticmethod 
    def searchRooms(query):
        results = {}
        for room_id in API.room_data.keys():
            if API.room_data[room_id]["room_name"].find(query) != -1:
                results[room_id] = API.room_data[room_id]
        return results

    #COMPUTER
    @staticmethod 
    def addComputer(computer):
        API.computer_data[str(uuid.uuid4())] = computer

    @staticmethod 
    def setComputer(id, computer):
        API.computer_data[id] = computer

    @staticmethod 
    def removeComputer(id):
        del API.computer_data[id]
        return API.saveData()

    @staticmethod 
    def getComputers():
        return API.computer_data

    @staticmethod 
    def getComputer(id):
        return API.computer_data[id]

    """
    Permet de trouver tous les ordinateurs dans une salle
    Renvoie un Dictionnaire avec les infos pour chaque ordinateur et son id comme clef
    """ 
    @staticmethod 
    def getComputersInRoom(roomId):
        results = {}
        for computer_key in list(API.computer_data.keys()):
            if API.computer_data[computer_key]["localisation"]["room_id"] == roomId:
                results[computer_key] = API.computer_data[computer_key]
        return results

    #SOFTWARE
    @staticmethod 
    def addSoftware(computer_id, software):
        API.computer_data[computer_id]['softwares'][str(uuid.uuid4())] = software

    @staticmethod 
    def setSoftware(computer_id, software_id, software):
        API.computer_data[computer_id]['softwares'][software_id] = software

    @staticmethod 
    def removeSoftware(computer_id, software_id):
        API.computer_data[computer_id]['softwares'].remove(software_id)

    @staticmethod 
    def getSoftwares(computer_id):
        return API.computer_data[computer_id]['softwares']

    @staticmethod 
    def getSoftware(computer_id, software_id):
        return API.computer_data[computer_id]['softwares'][software_id]

    #PLUGINS
    @staticmethod 
    def addPlugin(computer_id, software_id, plugin):
        API.computer_data[computer_id]['softwares'][software_id]['add_on'][str(uuid.uuid4())] = plugin

    @staticmethod 
    def setPlugin(computer_id, software_id, plugin_id, plugin):
        API.computer_data[computer_id]['softwares'][software_id]['add_on'][plugin_id] = plugin

    @staticmethod 
    def removePlugin(computer_id, software_id, plugin_id):
        API.computer_data[computer_id]['softwares'][software_id]['add_on'].remove(plugin_id)

    @staticmethod 
    def getPlugins(computer_id, software_id):
        return API.computer_data[computer_id]['softwares'][software_id]['add-on']

    @staticmethod 
    def getPlugin(computer_id, software_id, plugin_id):
        return API.computer_data[computer_id]['softwares'][software_id]['add-on'][plugin_id]