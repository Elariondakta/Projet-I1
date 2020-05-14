from __future__ import print_function, unicode_literals

from PyInquirer import style_from_dict, Token, prompt, print_json, Separator, Validator, ValidationError
from prettytable import PrettyTable
from utils import clear
from api import API
import style

class Rooms:
    def __init__(self): ##Métthode qui charge les données etc...
        self.base_data = API.getRooms()
        self.active_data = API.getRooms()


    def display(self):  ##Méthode qui lance l'affichage avec interaction etc...
        clear()
        print("*"*5, "Displaying rooms", "*"*5)
        self.display_options()

    def _checkSelectedIndex(self, val, data): ##Verifie qu'un id de salle existe bien
        try:
            if int(val) >= 0 and int(val) < len(data):
                return True
            else: return "Vous devez rentrer un index existant !"
        except:
            return "Vous devez rentrer un nombre !"

    def display_options(self): ##Formulaire initial des rooms
        
        options = [
            {
                'type': 'list',
                'name': 'action_choices',
                'message': "Que voulez vous faire ?",
                'choices': [
                    "Lister les salles",
                    "Effectuer une recherche",
                    "Lister les détails d'une salle",
                    "Créer une salle",
                    "Supprimer une salle",
                    Separator(),
                    "Retour",
                ]
            }
        ]
        res = prompt(options)["action_choices"]
        res_index = options[0]['choices'].index(res)
        if res_index == 0: ##Lister les salles
            self.display_table()
            self.display_options()

        elif res_index == 1: ##Effectuer une recherche
            self.display_search()
            self.display_options()
            
        elif res_index == 2: ##Ouvrir les détails d'une salle   
            room_id = self.form_get_id_room() ##Demande l'id de la salle
            self.display_room_detail(room_id) ##Ouvre le formulaire

        elif res_index == 3: ##Creer une salle
            self.createRoom()
            
        elif res_index == 4: ##Supprimer une salle
            self.display_delete()

    def display_table(self, disp_active = False): #On affiche la liste des salles
        table = PrettyTable()
        table.field_names = ["Id", "Bâtiment", "Salle"]

        i = 0
        for table_row_key in self.base_data.keys():
            if table_row_key not in list(self.active_data.keys()) and disp_active:
                i += 1
                continue
            else:
                table_row_el = self.base_data[table_row_key]
                table.add_row([i, table_row_el["building_name"], table_row_el["room_name"]])
                i += 1

        print(table)

    def display_search(self): ##Formulaire de recherche de salle
        options = [
            {
                'type': 'input',
                'name': 'search_query',
                'message': 'Rechercher une salle : ',
            },
        ]
        query = prompt(options)["search_query"]
        self.active_data = API.searchRooms(query)
        self.display_table(True)

    def form_get_id_room(self): ##Formulaire qui demande pour demander l'id d'une salle
        options = [
            {
                'type': 'input',
                "message": "Entrez l'identifiant de la salle",
                "name": 'get_id',
                "validate": lambda val: self._checkSelectedIndex(val, API.getRooms())
            }
        ]
        room_index = int(prompt(options)["get_id"])
        room_id = list(API.getRooms().keys())[room_index]
        
        return room_id ##On renvoie l'id de la salle stocké dans le json

    def display_delete(self): ##Formulaire de suppression de salle

        remove_id = self.form_get_id_room() ##Demande à l'user l'id de la salle
        
        confirm = [
            {
                'type': 'confirm',
                'name': "confirm",
                'message': "Etes-vous sur de supprimer la salle " + API.getRooms()[remove_id]["room_name"] + " ?"
            }
        ]
        res = prompt(confirm)["confirm"] ##Affiche le formulaire
        clear()

        ##Traitement de la réponse
        if res == True:
            API.removeRoom(remove_id) ##Suppression dans la BDD        
            print(style.green("La salle à bien été supprimée !"))
        else:
            print(style.red("Action annulée"))

        ##Afficher les options
        self.display_options()

    def createRoom(self): ##Formulaire de création de nouvelle salle
        options = [
            {
                'type': "input",
                "message": "Nom de la salle",
                "name": "room_name"
            },
            {
                'type': "input",
                "message": "Nom du bâtiment",
                "name": "building_name"
            }
        ]
        res = prompt(options) ##Affiche le formulaire
        API.addRoom(res["room_name"], res["building_name"]) ##Ajouter la salle dans la bdd
        clear()
        print(style.green("La salle à bien été ajoutée !"))
        self.display_options() ##Affiche les options


    def display_room_detail(self, room_id): ##Afficher les détails d'une salle
        
        room = API.getRoom(room_id) ##Demander l'id de la salle à l'utilisateur
        
        options = [
            {
                'type': 'list',
                'name': 'menu_room_detail',
                'message': 'Selectionner un des menus avec les flèches du clavier.',
                'choices': [
                    'Editer',
                    "Ordinateurs de la salle",
                    Separator(),
                    "Retour"
                ]
            },
        ]

        clear()
        print("Salle : " + room["room_name"])
        print("Batiment : " + room["building_name"])
        res = prompt(options) ##On affiche le formulaire

        try:
            res_index = options[0]['choices'].index(res["menu_room_detail"])
        except KeyError:
            res_index = 0

        if res_index == 0: ##Formulaire d'edition de la salle
            self.edit_room(room_id)

        elif res_index == 1: ##Formulaire des ordinateurs de la salle
            pass
            
        elif res_index == 3: ##Retour
            clear()
            self.display_options()

    def edit_room(self, room_id): ##Formulaire d'édition de la salle
        room = API.getRoom(room_id)

        option_name = [
            {
                'type': 'input',
                'name': 'edit_room_name',
                'message': 'Nom de la salle : ',
                'default': room["room_name"],
            }
        ]

        name = prompt(option_name)["edit_room_name"] ##Sauvegarde le nouveau nom dans variable

        option_building = [
            {
                'type': 'input',
                'name': 'edit_room_building',
                'message': 'Batiment : ',
                'default': room["building_name"],
            }
        ]

        building = prompt(option_building)["edit_room_building"] ##Sauvegarde le nouveau batiment dans variable

        new_room = {"room_name" : name, "building_name" : building} ##Creer objet de salle avec les nouvelles valeurs

        API.setRoom(room_id, new_room) ##On enregistre

        self.display_room_detail(room_id) ##On retourne sur le detail de la classe

