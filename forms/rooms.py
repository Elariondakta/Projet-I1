from PyInquirer import prompt, Separator, Validator, ValidationError
from prettytable import PrettyTable
from utils import clear
from api import API
class Rooms:
    def __init__(self): ##Métthode qui charge les données etc...
        self.base_data = API.getRooms()
        self.active_data = API.getRooms()
    def display(self):  ##Méthode qui lance l'affichage avec interaction etc...
        clear()
        print("*"*5, "Displaying rooms", "*"*5)
        self.display_options()

    def display_table(self, disp_active = False):
        table = PrettyTable()
        table.field_names = ["Id", "Bâtiment", "Salle"]
        i = 0
        print(self.active_data)
        for table_row_key in self.base_data.keys():
            if table_row_key not in list(self.active_data.keys()) and disp_active:
                i += 1
                continue
            else:
                table_row_el = self.active_data[table_row_key]
                table.add_row([i, table_row_el["building_name"], table_row_el["room_name"]])
                i += 1


        print(table)

    def display_options(self):
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
                ]
            }
        ]
        res = prompt(options)["action_choices"]
        res_index = options[0]['choices'].index(res)
        if res_index == 0:
            ##On liste les salles
            self.display_table()
            self.display_options()
        elif res_index == 1:
            ##On lance une recherche
            self.display_search()
            self.display_options()
        elif res_index == 2:
            options = [
                {
                    'type': 'input',
                    'name': 'search_query',
                    'message': 'Identifiant de la salle :',
                },
            ]
            query = prompt(options)["search_query"]
            self.display_room_detail(query)
        elif res_index == 3:
            ##On créer une salle
            pass
        elif res_index == 4:
            self.display_delete()
            ##On supprime une salle

    def display_search(self):
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

    def display_delete(self):
        # self.display_table()
        options = [
            {
                'type': 'input',
                "message": "Entrez l'Id de la salle à supprimer",
                "name": 'remove_id',
                "validate": lambda val: self._checkSelectedIndex(val, API.getRooms())
            }
        ]
        remove_index = int(prompt(options)["remove_id"])
        remove_id = list(API.getRooms().keys())[remove_index]
        confirm = [
            {
                'type': 'confirm',
                'name': "confirm",
                'message': "Etes-vous sur de supprimer la salle " + API.getRooms()[remove_id]["room_name"] + " ?"
            }
        ]
        res = prompt(confirm)["confirm"]
        if res == True:
            API.removeRoom(remove_id)
        self.display_options()

    def _checkSelectedIndex(self, val, data):
        try:
            if int(val) > 0 and int(val) < len(data):
                return True
            else: return "Vous devez rentrer un index existant !"
        except:
            return "Vous devez rentrer un nombre !"







    def display_room_detail(self, room_id):
        
        room = API.getRoom(room_id)
        
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
        while True:
            clear()
            print("Salle : " + room["room_name"])
            print("Batiment : " + room["building_name"])
            res = prompt(options)
            try:
                res_index = options[0]['choices'].index(res["menu_room_detail"])
            except KeyError:
                res_index = 0

            if res_index == 0:
                ##Afficher le gestionnaire des salles
                self.edit_room(room)
            elif res_index == 1:
                #Editer
                #self.edit_room(room)
                pass
                
            elif res_index == 2:
                #Gestion des ordinateurs
                rooms_handler = Rooms()
                rooms_handler.display()

            elif res_index == 3:
                rooms_handler = Rooms()
                rooms_handler.display()

    def edit_room(self, room):
        options = [
            {
                'type': 'editor',
                'name': 'edit_room_name',
                'message': 'Nom de la salle : ',
                'default' : room["room_name"],
                'validate' : lambda text:len(text.split('\n')) > 0 or 'Ne doit pas être vide.'
            },
        ]
        name = prompt(options)["edit_room_name"]

        options = [
            {
                'type': 'editor',
                'name': 'edit_room_building',
                'message': 'Batiment : ',
                'default' : room["building_name"],
                'validate' : lambda text:len(text.split('\n')) > 0 or 'Ne doit pas être vide.'
            },
        ]
        building = prompt(options)["edit_room_building"]
