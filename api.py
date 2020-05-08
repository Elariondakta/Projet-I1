# coding: utf-8 

import json, uuid
import logging
class API():

    choice_file = "./data/choice.json"

    computer_file = "./data/computers.json"

    room_file = "./data/rooms.json"

    software_file = "./data/softwares.json"

    @staticmethod 
    def loadData():
        with open(API.choice_file, 'r') as f:
            API.choice_data = json.load(f)

        with open(API.computer_file, 'r') as f:
            API.computer_data = json.load(f)
        
        with open(API.room_file, 'r') as f:
            API.room_data = json.load(f)

        with open(API.software_file, 'r') as f:
            API.software_data = json.load(f)

    @staticmethod 
    def saveData():
        try:
            with open(API.computer_file, 'w') as f:
                json.dump(API.computer_data, f)

            with open(API.room_file, 'w') as f:
                json.dump(API.room_data, f)

            with open(API.software_file, 'w') as f:
                json.dump(API.software_data, f)

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
    def setRoom(id, room):
        API.room_data[id] = room
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
    def addComputer(processor, ram, graphic_card, video_ports, screen, network_card, purchase, user, specs_tech, usb_data, nb_storage):
        API.computer_data[str(uuid.uuid4())] = {}
        return API.saveData()

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
    def addSoftware(name, editor, provider, version, licence_exp_date, add_on):
        API.software_data[str(uuid.uuid4())] = {
            "name": name,
            "editor": editor, 
            "provider": provider, 
            "version": version, 
            "licence_exp_date": licence_exp_date, 
            "add_on": add_on
        }
        return API.saveData()

    @staticmethod 
    def setSoftware(software_id, software):
        API.software_data[software_id] = software

    @staticmethod 
    def removeSoftware(software_id):
        del API.software_data[software_id]
        return API.saveData()

    @staticmethod 
    def getSoftwares():
        return API.software_data

    @staticmethod 
    def getSoftware(software_id):
        return API.software_data[software_id]

    @staticmethod 
    def searchSoftware(query):
        results = {}
        for software_id in API.software_data.keys():
            if API.room_data[software_id]["name"].find(query) != -1:
                results[software_id] = API.software_data[software_id]
        return results

    #PLUGINS
    @staticmethod 
    def addPlugin(software_id, plugin):
        API.software_data[software_id]['add_on'][str(uuid.uuid4())] = plugin

    @staticmethod 
    def setPlugin(software_id, plugin_id, plugin):
        API.software_data[software_id]['add_on'][plugin_id] = plugin

    @staticmethod 
    def removePlugin(software_id, plugin_id):
        API.software_data[software_id]['add_on'].remove(plugin_id)
        return API.saveData()

    @staticmethod 
    def getPlugins(software_id):
        return API.software_data[software_id]['add-on']

    @staticmethod 
    def getPlugin(software_id, plugin_id):
        return API.software_data[software_id]['add-on'][plugin_id]