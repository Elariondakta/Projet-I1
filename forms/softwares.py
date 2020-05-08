from PyInquirer import prompt, Separator
from prettytable import PrettyTable
from examples import custom_style_2
from utils import clear
from api import API
import datetime

class Software:
    def __init__(self): ##Métthode qui charge les données etc...
        pass

    def display(self):  ##Méthode qui lance l'affichage avec interaction etc...
        clear()
        print("*"*5, "Affichage des logiciels", "*"*5)
        self.display_table(API.getSoftwares()) 

    def display_options(self):
        options = [
            {
                'type': 'list',
                'name': 'action_choices',
                'message': "Que voulez vous faire ?",
                'choices': [
                    "Effectuer une recherche",
                    "Lister les détails d'un logiciel",
                    "Ajouter un logiciel",
                    "Supprimer un loficiel",
                ]
            }
        ]
        res = prompt(options)["action_choices"]
        res_index = options[0]['choices'].index(res)
        if res_index == 0:
            ##On lance une recherche
            self.display_search()
        elif res_index == 1:
            ##On liste les détails d'un logiciel
            pass
        elif res_index == 2:
            # On ajoute un logiciel
            self.addSoftware()
        elif res_index == 3:
            self.display_delete()
        
    
    def display_search(self):
        options = [
            {
                'type': 'input',
                'name': 'search_query',
                'message': 'Rechercher un logiciel : ',
            },
        ]
        query = prompt(options)["search_query"]
        self.display_table(API.searchSoftware(query)) 

    def checkStrLenght(self, str):
        if len(str)>0:
            return True
        else:
            return "Veillez entrez une valeur"

    def addSoftware(self):
        addOn = []
        questions = [
        {
            'type': 'input',
            'qmark':'',
            'name': 'name',
            'message': 'Quel est le nom du logiciel? ', 
            'validate': lambda val: self.checkStrLenght(val)
        },
        {
            'type': 'input',
            'qmark':'',
            'name': 'editor',
            'message': 'Quel est sont éditeur? ',
            'validate': lambda val: self.checkStrLenght(val)
        },
        {
            'type': 'input',
            'qmark':'',
            'name': 'provider',
            'message': 'Quel est son fournisseur? ', 
            'validate': lambda val: self.checkStrLenght(val) 
        },
        {
            'type': 'input',
            'qmark':'',
            'name': 'version',
            'message': "Quelle est sa version ? ", 
            'validate': lambda val: self.checkStrLenght(val)
        },
        {
            'type': 'input',
            'qmark':'',
            'name': 'licence_exp_date',
            'message': 'Quelle est la date d\'expiration de la license ? ', 
            'validate': lambda val: self.checkStrLenght(val)
        },
        {
            'type': 'list',
            'qmark':'',
            'name': 'numberOfAddOn',
            'message': 'Compbien de plugg-in contient de logiciel',
            'choices': ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9' , '10']
        },
        ]
        newSoftware = prompt(questions)
        for i in range (0, int(newSoftware['numberOfAddOn'])):
            addOnCharacteristic = [
                {
                    'type': 'input',
                    'qmark':'',
                    'name': 'nom',
                    'message': 'Quel est le nom du Plugg-in ? ', 
                    'validate': lambda val: self.checkStrLenght(val)
                }, 
                {
                    'type': 'input',
                    'qmark':'',
                    'name': 'editeur',
                    'message': 'Quel est son éditeur ? ', 
                    'validate': lambda val: self.checkStrLenght(val)
                }, 
                {
                    'type': 'input',
                    'qmark':'',
                    'name': 'providor',
                    'message': 'Quel est son fournisseur ? ', 
                    'validate': lambda val: self.checkStrLenght(val)
                }, 
                {
                    'type': 'input',
                    'qmark':'',
                    'name': 'nom',
                    'message': 'Quelle est sa version ? ', 
                    'validate': lambda val: self.checkStrLenght(val)
                }
            ]
            print(Separator())
            newAddOnCarateristic = prompt(addOnCharacteristic)
            addOn.append(newAddOnCarateristic)
        newSoftware['add_on']=addOn
        newSoftware['licence_exp_date']=int(newSoftware['licence_exp_date']) #TRES MOCHE A ENLEVER EN FAISANT LES TEST
        API.addSoftware(newSoftware["name"], newSoftware["editor"], newSoftware["provider"], newSoftware["version"], newSoftware["licence_exp_date"], newSoftware["add_on"])
        clear()
        print(Separator("Le logiciel à bien été ajoutée !"))
    
    def display_table(self, data):
        table = PrettyTable()
        table.field_names = ["ID", "Nom", "Editeur"] #,"Date d'expiraion de la lisence"
        i = 0
        for table_row_key in data.keys():
            table_row_el = data[table_row_key]
            table.add_row([i, table_row_el["name"], table_row_el["editor"]]) #, datetime.date.fromtimestamp(table_row_el["licence_exp_date"])
            i += 1
        print(table)
        self.display_options()

    def form_get_id_soft(self): ##Formulaire qui demande pour demander l'id d'une salle
        options = [
            {
                'type': 'input',
                "message": "Entrez l'identifiant du logiciel",
                "name": 'get_id',
                "validate": lambda val: self._checkSelectedIndex(val, API.getSoftwares())
            }
        ]
        soft_index = int(prompt(options)["get_id"])
        soft_id = list(API.getSoftwares().keys())[room_index]

    def display_delete(self): ##Formulaire de suppression de logiciel

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

    def _checkSelectedIndex(self, val, data):
        try:
            if int(val) > 0 and int(val) < len(data):
                return True
            else: return "Vous devez rentrer un index existant !"
        except:
            return "Vous devez rentrer un nombre !"
