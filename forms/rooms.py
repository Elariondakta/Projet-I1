from PyInquirer import prompt
from prettytable import PrettyTable
from utils import clear
from api import API
class Rooms:
    def __init__(self): ##Métthode qui charge les données etc...
        pass

    def display(self):  ##Méthode qui lance l'affichage avec interaction etc...
        clear()
        print("*"*5, "Displaying rooms", "*"*5)
        self.display_table(API.getRooms())

    def display_table(self, data):
        table = PrettyTable()
        table.field_names = ["Id", "Bâtiment", "Salle"]
        i = 0
        for table_row_key in data.keys():
            table_row_el = data[table_row_key]
            table.add_row([i, table_row_el["building_name"], table_row_el["room_name"]])
            i += 1

        print(table)
        self.display_options()

    def display_options(self):
        options = [
            {
                'type': 'list',
                'name': 'action_choices',
                'message': "Que voulez vous faire ?",
                'choices': [
                    "Effectuer une recherche",
                    "Lister les détails d'une salle",
                    "Supprimer une salle",
                    "Rennommer une salle"
                ]
            }
        ]
        res = prompt(options)["action_choices"]
        res_index = options[0]['choices'].index(res)
        if res_index == 0:
            ##On lance une recherche
            self.display_search()
        elif res_index == 1:
            ##On liste les détails d'une salle
            pass
        elif res_index == 2:
            ##On supprime une salle
            pass
        elif res_index == 3:
            ##On renomme une salle 
            pass

    def display_search(self):
        options = [
            {
                'type': 'input',
                'name': 'search_query',
                'message': 'Rechercher une salle : ',
            },
        ]
        query = prompt(options)["search_query"]
        self.display_table(API.searchRooms(query))

    def display_delete(self):
        options = [
            {
                'type': 'when',
                "message": "Entrez l'Id de la salle à supprimer",
                "name": 'remove_id'
            }
        ]
        remove_index = prompt(options)["remove_id"]
        remove_id = API.getRooms().keys()[remove_index]
        print(remove_id)
        API.removeRoom(remove_id)
        self.display_table(API.getRooms())


