from PyInquirer import prompt
from prettytable import PrettyTable
from utils import clear
from api import API
from datetime import datetime
class Computers :
    def __init__(self): ##Métthode qui charge les données etc...
        self.base_data = API.getComputers()
        self.active_data = API.getComputers()
        pass

    def display(self):  ##Méthode qui lance l'affichage avec interaction etc...
        clear()
        self.display_options()

    def _checkSelectedIndex(self, val, maxValue):
        try:
            if int(val) >= 0 and int(val) <= maxValue:
                return True
            else: return "Vous devez rentrer un nombre entre 0 et"+ str(maxValue) +"."
        except:
            return "Vous devez rentrer un nombre."

    def _checkDate(self, val):
        date_format = '%d/%m/%Y'
        try:
            datetime.strptime(val, date_format)
        except ValueError:
            return "Format incorrect, la date doit etre de la forme JJ/MM/AAAA"
        return True

    def display_options(self):
        options = [
            {
                'type': 'list',
                'name': 'action_choices',
                'message': "Que voulez vous faire ?",
                'choices': [

                    "Ajouter un ordinateur",
                    "Supprimer un ordinateur",
                    "Rennommer un ordinateur",
                    "Lister les ordinateurs",
                    "Lister les détails d'un ordinateur",
                    "Ajouter un software à un ordinateur",
                    "Effectuer une recherche"
                ]
            }
        ]
        res = prompt(options)["action_choices"]
        res_index = options[0]['choices'].index(res)
        if res_index == 0:
            ##On ajoute un ordi
            self.addComputer ()
        elif res_index == 1:
            ##On supprime un ordi
            self.remove_display()
            pass
        elif res_index == 2:
            ##On renomme un ordi
            pass
        elif res_index == 3:
            ##On liste les ordis 
            self.display_tables()
            self.display_options()
            pass
        elif res_index == 4:
            ##On liste les détails d'un ordi
            pass
        elif res_index == 5:
            ##On ajoute un software à un ordi
            pass
        elif res_index == 6:
            ##On effectue une recherche 
            pass

    def addComputer (self):
        processor = [
            {
                'type': 'input',
                'name': 'plateform',
                'message': 'Platforme du processeur:',
                'validate': lambda val: True if val == "32" or val == "64" else "Veuillez rentrer '32' ou '64' bits"
            },
            {
                'type': 'input',
                'name': 'brand',
                'message': 'Marque du processeur :',
            },
            {
                'type': 'input',
                'name': 'speed',
                'message': 'Vitese du processeur :',
            },
            {
                'type': 'input',
                'name': 'size_cache',
                'message': 'Taille du Cache :',
            },
            {
                'type': 'input',
                'name': 'model',
                'message': 'Modèle de processeur :',
            }
        ]
        RAM = [
            {
                'type': 'input',
                'name': 'number',
                'message': 'Nombre de RAM :',
                'validate': lambda val: self._checkSelectedIndex(val, 10)

            },
            {
                'type': 'input',
                'name': 'total_size',
                'message': 'Taille totale de la RAM :',
            }
        ]
        graphic_card = [
            {
                'type': 'input',
                'name': 'brand',
                'message': 'Marque de la carte graphique :',
            },
            {
                'type': 'input',
                'name': 'memory',
                'message': 'Taille Mémoire de la carte graphique :',
            },
            {
                'type': 'input',
                'name': 'model',
                'message': 'Modèle de la carte graphique :',
            }
        ]
        video_ports = [
            {
                'type': 'checkbox',
                'message': 'Selectionner les ports disponibles',
                'name': 'video_port',
                'choices': [ 
                    {
                        'name': 'VGA'
                    },
                    {
                        'name': 'HDMI'
                    },
                    {
                        'name': 'Display-Port'
                    },
                    {
                        'name': 'DVI-A'
                    },
                    {
                        'name': 'DVI-D'
                    },
                    {
                        'name': 'USB-C'
                    }
                ]
            }
        ]
        screen = [
            {
                'type': 'input',
                'name': 'screen_res',
                'message': "Résolution de l'écran :",
                'validate': lambda val: self._checkSelectedIndex(val, 10000)
            },
            {
                'type': 'input',
                'name': 'screen_size_x',
                'message': "Largeur de l'écran (en px) :",
                'validate': lambda val: self._checkSelectedIndex(val, 10000)
            },
            {
                'type': 'input',
                'name': 'screen_size_y',
                'message': "Longueur de l'écran (en px) :",
                'validate': lambda val: self._checkSelectedIndex(val, 30000)
            }
        ]
        network_card = [
            {
                'type': 'input',
                'name': 'speed',
                'message': 'Vitesse de la carte réseau :',
            },
            {
                'type': 'input',
                'name': 'brand',
                'message': 'Marque de la carte réseau :',
            }
        ]
        purchase = [
            {
                'type': 'input',
                'name': 'maker',
                'message': "Fabricant de l'ordinateur:",
            },
            {
                'type': 'input',
                'name': 'provider',
                'message': "Fournisseur de l'ordinateur:",
            },
            {
                'type': 'input',
                'name': 'purchase_date_timestamp',
                'message': "Date d'achat :",
                'validate': lambda val: self._checkDate(val)
            }
        ]

        user = [
            {
                'type': 'input',
                'name': 'name',
                'message': 'Nom :',
            },
            {
                'type': 'input',
                'name': 'username',
                'message': "Nom d'utilisateur :",
            }
        ]
        specs_tech = [
            {
                'type': 'checkbox',
                'message': 'Selectionner les characteristiques technique',
                'name': 'specs_tech',
                'choices': [ 
                    {
                        'name': 'Lecteur CD'
                    },
                    {
                        'name': 'Wifi'
                    },
                    {
                        'name': 'Bluetooth'
                    }
                ]
            }
        ]
        USB = [
            {
                'type': 'input',
                'name': 'nb_USB_port',
                'message': "Combien l'ordinateur à t'il de ports USB ? :",
                'validate': lambda val: self._checkSelectedIndex(val, 10)
            }
        ]
        nbStorage = [
            {
                'type': 'input',
                'name': 'nb_storage',
                'message': "Combien d'espaces de stockage l'ordinateur a t'il ? :",
                'validate': lambda val: self._checkSelectedIndex(val, 10)
            }
        ]
        
        processorData = prompt(processor)
        RAMData = prompt(RAM)
        graphic_cardData = prompt(graphic_card)
        video_portsData = prompt(video_ports)
        screenData = prompt(screen)
        network_cardData = prompt(network_card)
        purchaseData = prompt(purchase)
        userData = prompt(user)
        specs_techData = prompt(specs_tech)
        USBData = int(prompt(USB)["nb_USB_port"])
        nbStorageData = int(prompt(nbStorage)["nb_storage"])
        
        storageData = []

        for i in range(0, nbStorageData):
            storageData.append(prompt([
                {
                    'type': 'input',
                    'name': 'port',
                    'message': 'Port n° :',
                    'validate': lambda val: self._checkSelectedIndex(val, 10)
                },
                {
                    'type': 'input',
                    'name': 'type',
                    'message': 'Type :',
                },
                {
                    'type': 'input',
                    'name': 'size',
                    'message': 'Taille :',
                }
            ]))
        
        confirm = [
            {
                'type': 'confirm',
                'name': "confirm",
                'message': "Confirmer l'ajout de l'ordinateur"
            }
        ]
        confirmData = prompt(confirm)

        if confirmData == True: 
            API.addComputer(processorData, RAMData, graphic_cardData, video_portsData, screenData, network_cardData, purchaseData, userData, specs_techData, USBData, nbStorageData)
            
    def remove_display(self):
        options = [
            {
                'type': 'input',
                "message": "Entrez l'Id de l'ordinateur à supprimer",
                "name": 'remove_id',
                "validate": lambda val: self._checkSelectedIndex(val, len(self.base_data))
            }
        ]
        remove_index = int(prompt(options)["remove_id"])
        remove_id = list(API.getComputers().keys())[remove_index]
        confirm = [
            {
                'type': 'confirm',
                'name': "confirm",
                'message': "Etes-vous sur de supprimer l'ordinateur de " + API.getComputers()[remove_id]["user"]["name"] +" ?"
            }
        ]
        res = prompt(confirm)["confirm"]
        if res == True:
            API.removeComputer(remove_id)
        self.display_options()

    def display_tables(self, disp_active = False):
        table = PrettyTable()
        table.field_names = ["Id", "Utilisateurs", "Logiciels", "Localisation"]
        i = 0
        for table_row_key in self.base_data.keys():
            if table_row_key not in list(self.active_data.keys()) and disp_active:
                i += 1
                continue
            else:
                table_row_el = self.active_data[table_row_key]
                room_el = API.getRoom(table_row_el["localisation"])
                table.add_row([
                    i, 
                    table_row_el["user"]["username"], 
                    str(len(table_row_el["softwares"])) + " logiciel(s) installé(s)",
                    room_el["room_name"]
                ])
                i += 1
        print(table)
        