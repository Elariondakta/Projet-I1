from PyInquirer import prompt, Separator
from prettytable import PrettyTable
from examples import custom_style_2
from utils import clear
from api import API
from datetime import datetime, date
import style
import uuid

class Software:


    def __init__(self): ##Métthode qui charge les données 
        self.base_data = API.getSoftwares()
        self.active_data = API.getSoftwares()


    def display(self):  ##Méthode qui lance l'affichage avec interaction etc...
        clear()
        print("*"*5, "Affichage des logiciels", "*"*5)
        self.display_table(API.getSoftwares()) 

    def _checkDate(self, val): ##Fonction qui permet de vérifier le format de la date saisie
        date_format = '%d/%m/%Y'
        try:
            datetime.strptime(val, date_format) #Convertit la date en timestamp
        except ValueError:
            return "Format incorrect, la date doit etre de la forme JJ/MM/AAAA"
        return True

    def display_options(self): #affichage du menu
        print("\n" + "*"*5, "Menu :", "*"*5 + "\n")

        options = [
            {
                'type': 'list',
                'name': 'action_choices',
                'message': "Que voulez vous faire ?",
                'choices': [
                    "Lister les logiciels",
                    "Rechercher un logiciel",
                    "Lister les détails d'un logiciel",
                    "Ajouter un logiciel",
                    "Supprimer un logiciel",
                    "Retour"
                ]
            }
        ]      

        try:

            res = prompt(options)["action_choices"]
            res_index = options[0]['choices'].index(res)
            # différentes options de la recherche
            if res_index == 1:
                ##affiche la recherche
                self.display_search()
            elif res_index == 0:
                ##affiche la liste des logiciels
                self.display_table()
            elif res_index == 2:
                self.display_detail()
                ##On liste les détails d'un logiciel
                pass
            elif res_index == 3:
                # On ajoute un logiciel
                self.addSoftware()
            elif res_index == 4:
                self.display_delete()
            elif res_index == 5:
                pass
        except:
            clear()
            self.display()

    def display_search(self): ##Formulaire de recherche de logiciel
            options = [
                {
                    'type': 'input',
                    'name': 'search_query',
                    'message': 'Rechercher un logiciel : ',
                },
            ]
            query = prompt(options)["search_query"] #affichage des options
            self.active_data = API.searchSoftware(query) #Récupère le logiciel
            self.display_table(True) #Affiche le logiciel
            self.display_options() #Affiche les options

    def checkStrLenght(self, str): #méthode qui vérifie qu'il y a bien une chaine de caractère rentrée
        if len(str)>0:
            return True
        else:
            return "Veillez entrez une valeur"

    def addSoftware(self): #méthode pour ajouter un software
        addOn = {} #réinitialise d'éventueles variables restantes
        questions = [ #liste des questions
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
            'validate': lambda val: self._checkDate(val)
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
        for _ in range (0, int(newSoftware['numberOfAddOn'])): #pour chaque ADD-ON déclarer
            addOnCharacteristic = [
                {
                    'type': 'input',
                    'qmark':'',
                    'name': 'name',
                    'message': 'Quel est le nom du Plugg-in ? ', 
                    'validate': lambda val: self.checkStrLenght(val)
                }, 
                {
                    'type': 'input',
                    'qmark':'',
                    'name': 'editor',
                    'message': 'Quel est son éditeur ? ', 
                    'validate': lambda val: self.checkStrLenght(val)
                }, 
                {
                    'type': 'input',
                    'qmark':'',
                    'name': 'provider',
                    'message': 'Quel est son fournisseur ? ', 
                    'validate': lambda val: self.checkStrLenght(val)
                }, 
                {
                    'type': 'input',
                    'qmark':'',
                    'name': 'version',
                    'message': 'Quelle est sa version ? ', 
                    'validate': lambda val: self.checkStrLenght(val)
                }
            ]
            print(Separator())
            newAddOnCarateristic = prompt(addOnCharacteristic)
            addOn[str(uuid.uuid4())]=newAddOnCarateristic #créer un identifiant unique pour l'addOn et l'ajoute au dictionnaire des add on de ce logiciel
        newSoftware['add_on']=addOn #ajoute les addON au logiciel
        date_format = '%d/%m/%Y'
        newSoftware['licence_exp_date'] = datetime.strptime(newSoftware['licence_exp_date'], date_format).timestamp()
        API.addSoftware(newSoftware) #ajoute le logiciel à la base de données
        clear()
        print(Separator("Le logiciel à bien été ajoutée !"))
    
    def display_table(self, disp_active = False):
        table = PrettyTable()
        table.field_names = ["ID", "Nom", "Editeur","Date d'expiration de la licence"]

        i = 0
        for table_row_key in self.base_data.keys(): #méthode pour permettre la création des ID de l'affichage
            if table_row_key not in list(self.active_data.keys()) and disp_active:
                i += 1
                continue
            else:
                table_row_el = self.base_data[table_row_key]
                table.add_row([i, table_row_el["name"], table_row_el["editor"], date.fromtimestamp(table_row_el["licence_exp_date"])])
                i += 1

        print(table)
        self.display_options()

    def form_get_id_soft(self): ##Formulaire qui demande pour demander l'id d'une salle
        options = [ #affiche les options
            {
                'type': 'input',
                "message": "Entrez l'identifiant du logiciel",
                "name": 'get_id',
                "validate": lambda val: self._checkSelectedIndex(val, API.getSoftwares())
            }
        ]
        soft_index = int(prompt(options)["get_id"])
        soft_id = list(API.getSoftwares().keys())[soft_index] #récupère l'identifiant du loficiel
        return soft_id

    def display_delete(self): ##Formulaire de suppression de logiciel

        remove_id = self.form_get_id_soft() ##Demande à l'user l'id du logiciel
        
        confirm = [ #méthode de confirmation
            {
                'type': 'confirm',
                'name': "confirm",
                'message': "Etes-vous sur de supprimer le logiciel " + API.getSoftwares()[remove_id]["name"] + " ?"
            }
        ]
        res = prompt(confirm)["confirm"] ##Affiche le formulaire
        clear()

        ##Traitement de la réponse
        if res == True:
            API.removeSoftware(remove_id) ##Suppression dans la BDD        
            print(style.green("Le logiciel à bien été supprimée !"))
        else:
            print(style.red("Action annulée"))

        ##Afficher les options
        self.display_options()

    def _checkSelectedIndex(self, val, data): #méthode qui vérifie l'index rentré
        try:
            if int(val) >= 0 and int(val) < len(data):
                return True
            else: return "Vous devez rentrer un index existant !"
        except:
            return "Vous devez rentrer un nombre !"

    def display_detail(self): #méthode qui affiche les détails du programme
        soft_id = self.form_get_id_soft() #récupère l'identifiant du programe dont il faut afficher les détails 
        soft = API.getSoftware(soft_id) #récupère le logiciel
        clear() 
        #affiche les détails
        print("- Nom : " + soft["name"])
        print("- Fournisseur : " + soft["provider"])
        print("- Editeur : " + soft["editor"])
        print("- Version : " + soft["version"])
        print("- Date d'expiration de la license : " + str(date.fromtimestamp(soft["licence_exp_date"]))) #converti la date en format jour mois année
        add_on_of_software = soft["add_on"]
        i = 0
        for software_key in add_on_of_software.keys():
            print("-"*5+"Plug-in "+str(i+1)+"-"*5)
            print("- Nom : " + add_on_of_software[software_key]["name"])
            print("- Editeur : " + add_on_of_software[software_key]["editor"])
            print("- Fournisseur : " + add_on_of_software[software_key]["provider"])
            print("- Version : " + add_on_of_software[software_key]["version"])
            i += 1

        options = [
            {
                'type': 'list',
                'name': 'action_choices',
                'message': "Voulez vous affichez la liste des ordinateur sur lequel ce logiciel est installé ?",
                'choices': [
                    "Oui",
                    "Non"
                ]
            }
        ]
        try:
            res = prompt(options)["action_choices"] #affiche les options
            res_index = options[0]['choices'].index(res) #récupère les résultats 
            if res_index == 0: #si oui
                print("\n" + "*"*5, "Ordinateurs possédant ce logiciel :", "*"*5 + "\n")
                computer_list = API.getComputersFromSoftware(soft_id) #récupère les ordi sur lequel ce logiciel est installé
                table = PrettyTable()
                table.field_names = ["Id", "Nom", "Utilisateur", "Logiciels"]
                i = 0
                for table_row_key in computer_list:         #Pour chaque ordinateur de la liste
                    table_row_el = computer_list[table_row_key]  #Sinon on affiche les données
                    table.add_row([
                        i, 
                        table_row_el["name"],
                        table_row_el["user"]["username"], 
                        str(len(table_row_el["softwares"])) + " logiciel(s) installé(s)"
                    ])
                    i += 1
                print(table)


            elif res_index == 1:
                clear()

            self.display_options()
        except:
            self.display_detail()