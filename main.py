from api import API
from utils import clear
from PyInquirer import prompt, Separator
from forms.rooms import Rooms
from forms.softwares import Software
from forms.computers import Computers
import sys


if __name__ == '__main__':
    """
    Chargement des données
    """
    API.loadData()
    options = [
        {
            'type': 'list',
            'name': 'menu_choice',
            'message': 'Selectionner un des menus avec les flèches du clavier.',
            'choices': [
                'Gestionnaire de salles',
                "Gestionnaire d'ordinateurs",
                "Gestionnaire des softwares",
                Separator(),
                "Quitter"
            ]
        },
    ]
    while True:
        clear()
        
        try:
            res = prompt(options)
            res_index = options[0]['choices'].index(res["menu_choice"])
        

            if res_index == 0:
                ##Afficher le gestionnaire des salles
                rooms_handler = Rooms()
                rooms_handler.display()
            elif res_index == 1:
                ##Afficher le gestionnaire des ordinateurs
                computers_handler = Computers()
                computers_handler.display()
                pass
            elif res_index == 2:
                ##Afficher le gestionnaire des softwares
                software_handler = Software()
                software_handler.display()
            elif res_index == 4:    ##Fonction pour quiter
                break

        except:
            pass