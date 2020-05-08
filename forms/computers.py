from PyInquirer import prompt, Separator
from prettytable import PrettyTable
from utils import clear
from api import API
from datetime import datetime
import style

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

    def _convertDate(self, val):
        return datetime.strptime(val, '%d/%m/%Y').timestamp()

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
            self.display_computer_detail()

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
                'message': "Date d'achat (au format JJ/MM/AAAA):",
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
        purchaseData["purchase_date_timestamp"] = self._convertDate(purchaseData["purchase_date_timestamp"])
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
        confirmData = prompt(confirm)["confirm"]

        if confirmData: 
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
                try:
                    room_el = API.getRoom(table_row_el["localisation"])["room_name"]
                except KeyError:
                    room_el = "Pas de salle spécifiée"
                table.add_row([
                    i, 
                    table_row_el["user"]["username"], 
                    str(len(table_row_el["softwares"])) + " logiciel(s) installé(s)",
                    room_el
                ])
                i += 1
        print(table)
        



    def display_computer_detail(self, computer_id = "pc1779"):
    
        computer = API.getComputer(computer_id) ##Demander l'id de l'ordi à l'utilisateur
        
        options = [
            {
                'type': 'list',
                'name': 'menu_computer_detail',
                'message': 'Selectionner un des menus avec les flèches du clavier.',
                'choices': [
                    'Editer',
                    "Logiciels installés",
                    Separator(),
                    "Retour"
                ]
            },
        ]

        clear()
        print("Ordinateur : " + computer_id + "\n")
        print(Separator())
        print(style.bold("\nSpécifications techniques :"))

        #Computer
        print(style.blue("\nProcesseur :"))
        print(style.light_cyan("\t" + "Architecture : ") + computer["specs"]["processor"]["plateform"] + " bits")
        print(style.light_cyan("\t" + "Marque : ") + computer["specs"]["processor"]["brand"])
        print(style.light_cyan("\t" + "Vitesse : ") + computer["specs"]["processor"]["speed"])
        print(style.light_cyan("\t" + "Cache : ") + computer["specs"]["processor"]["size_cache"])
        print(style.light_cyan("\t" + "Modèle : ") + computer["specs"]["processor"]["model"])

        #RAM
        print(style.blue("\nRAM :"))
        print(style.light_cyan("\t" + "Nombre de barette : ") + computer["specs"]["RAM"]["number"])
        print(style.light_cyan("\t" + "Taille : ") + computer["specs"]["RAM"]["total_size"])

        #Graphic card
        print(style.blue("\nCarte graphique :"))
        print(style.light_cyan("\t" + "Marque : ") + computer["specs"]["graphic_card"]["brand"])
        print(style.light_cyan("\t" + "Mémoire : ") + computer["specs"]["graphic_card"]["memory"])
        print(style.light_cyan("\t" + "Modèle : ") + computer["specs"]["graphic_card"]["model"])

        #Video port
        print(style.blue("\nPorts vidéo :"))
        print(style.light_cyan("\t" + "Ports vidéo : ") + ', '.join(computer["specs"]["video_port"]))

        #Screen
        print(style.blue("\nEcran :"))
        print(style.light_cyan("\t" + "Résolution : ") + computer["specs"]["screen"]['screen_res'])
        print(style.light_cyan("\t" + "Taille : ") + str(computer["specs"]["screen"]['screen_size']).strip('[]').replace(', ', 'x') + "px")

        #Connectors
        print(style.blue("\nConnectique :"))
        print(style.light_cyan("\t" + "Lecteur CD : ") + "Oui" if  computer["specs"]["CD_player"] else "Non" )
        print(style.light_cyan("\t" + "Ports USB : ") + computer["specs"]["nb_USB_port"])

        #Stockage
        print(style.blue("\nStockage :"))

        n_storage = 1
        for storage in computer["specs"]['storage']:
            print(style.light_cyan("\tStockage " + str(n_storage) + " :"))
            print(style.magenta("\t\tType : ") + storage["type"])
            print(style.magenta("\t\tPort : ") + str(storage["port"]))
            print(style.magenta("\t\tTaille : ") + str(storage["size"]))
            n_storage+=1

        #Network card
        print(style.blue("\nCarte réseau :"))
        print(style.light_cyan("\t" + "Vitesse : ") + computer["specs"]["network_card"]['speed'])
        print(style.light_cyan("\t" + "Marque : ") + computer["specs"]["network_card"]['brand'])

        #User
        print(style.blue("\nUtilisateur :"))
        print(style.light_cyan("\t" + "Nom : ") + computer["user"]['name'])
        print(style.light_cyan("\t" + "Nom  d'utilisation : ") + computer["user"]['username'])

        #Other
        print(style.blue("\nAutre :"))
        print(style.light_cyan("\t" + "WiFi : ") + "Oui" if  computer["specs"]["wifi"] else "Non" )
        print(style.light_cyan("\t" + "Bluetooth : ") + "Oui" if  computer["specs"]["bluetooth"] else "Non" )
        print(style.light_cyan("\t" + "Fabriquant : ") + computer["specs"]["maker"])
        print(style.light_cyan("\t" + "Fournisseur : ") + computer["specs"]["provider"])
        print(style.light_cyan("\t" + "Date d'achat : ") + datetime.fromtimestamp(computer["specs"]["purchase_date_timestamp"]).strftime("%d/%m/%Y"))

        print("\n")
        print(Separator())

        print(style.bold("\nLocalisation :\n"))
        print(style.blue("Salle :"))
        print(style.light_cyan("\t" + "Nom : ") + API.getRoom(computer["localisation"])["room_name"])
        print(style.light_cyan("\t" + "Batiment : ") + API.getRoom(computer["localisation"])["building_name"])

        print("\n")
        print(Separator())
        print("\n")

        res = prompt(options) ##On affiche le formulaire

        try:
            res_index = options[0]['choices'].index(res["menu_computer_detail"])
        except KeyError:
            res_index = 0

        if res_index == 0: ##Formulaire d'edition de l'ordinateur
            self.edit_computer_detail(computer_id)
        elif res_index == 1: ##Formulaire des logiciels
            pass
            
        elif res_index == 3: ##Retour
            clear()
            #self.display_options()


    def edit_computer_detail(self, computer_id):
        computer = API.getComputer(computer_id)

        processor = [
            {
                'type': 'input',
                'name': 'plateform',
                'message': 'Platforme du processeur:',
                'validate': lambda val: True if val == "32" or val == "64" else "Veuillez rentrer '32' ou '64' bits",
                'default' : str(computer["specs"]["processor"]["plateform"])
            },
            {
                'type': 'input',
                'name': 'brand',
                'message': 'Marque du processeur :',
                'default' : str(computer["specs"]["processor"]["brand"])
            },
            {
                'type': 'input',
                'name': 'speed',
                'message': 'Vitese du processeur :',
                'default' : str(computer["specs"]["processor"]["speed"])
            },
            {
                'type': 'input',
                'name': 'size_cache',
                'message': 'Taille du Cache :',
                'default' : str(computer["specs"]["processor"]["size_cache"])
            },
            {
                'type': 'input',
                'name': 'model',
                'message': 'Modèle de processeur :',
                'default' : str(computer["specs"]["processor"]["model"])
            }
        ]
        RAM = [
            {
                'type': 'input',
                'name': 'number',
                'message': 'Nombre de RAM :',
                'validate': lambda val: self._checkSelectedIndex(val, 10),
                'default' : str(computer["specs"]["RAM"]["number"])

            },
            {
                'type': 'input',
                'name': 'total_size',
                'message': 'Taille totale de la RAM :',
                'default' : str(computer["specs"]["RAM"]["total_size"])
            }
        ]
        graphic_card = [
            {
                'type': 'input',
                'name': 'brand',
                'message': 'Marque de la carte graphique :',
                'default' : str(computer["specs"]["graphic_card"]["brand"])
            },
            {
                'type': 'input',
                'name': 'memory',
                'message': 'Taille Mémoire de la carte graphique :',
                'default' : str(computer["specs"]["graphic_card"]["memory"])               
            },
            {
                'type': 'input',
                'name': 'model',
                'message': 'Modèle de la carte graphique :',
                'default' : str(computer["specs"]["graphic_card"]["model"])
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
                'validate': lambda val: self._checkSelectedIndex(val, 10000),
                'default' : str(computer["specs"]["screen"]["screen_res"])
            },
            {
                'type': 'input',
                'name': 'screen_size_x',
                'message': "Largeur de l'écran (en px) :",
                'validate': lambda val: self._checkSelectedIndex(val, 10000),
                'default' : str(computer["specs"]["screen"]["screen_size"][0])
            },
            {
                'type': 'input',
                'name': 'screen_size_y',
                'message': "Longueur de l'écran (en px) :",
                'validate': lambda val: self._checkSelectedIndex(val, 30000),
                'default' : str(computer["specs"]["screen"]["screen_size"][1])
            }
        ]
        network_card = [
            {
                'type': 'input',
                'name': 'speed',
                'message': 'Vitesse de la carte réseau :',
                'default' : str(computer['specs']["network_card"]["speed"])
            },
            {
                'type': 'input',
                'name': 'brand',
                'message': 'Marque de la carte réseau :',
                'default' : str(computer['specs']["network_card"]["brand"])
            }
        ]
        purchase = [
            {
                'type': 'input',
                'name': 'maker',
                'message': "Fabricant de l'ordinateur:",
                'default' : str(computer['specs']["maker"])
            },
            {
                'type': 'input',
                'name': 'provider',
                'message': "Fournisseur de l'ordinateur:",
                'default' : str(computer['specs']["provider"])
            },
            {
                'type': 'input',
                'name': 'purchase_date_timestamp',
                'message': "Date d'achat :",
                'validate': lambda val: self._checkDate(val),
                'default' : str(datetime.fromtimestamp(computer["specs"]["purchase_date_timestamp"]).strftime("%d/%m/%Y"))
            }
        ]

        user = [
            {
                'type': 'input',
                'name': 'name',
                'message': 'Nom :',
                'default' : str(computer["user"]['name'])
            },
            {
                'type': 'input',
                'name': 'username',
                'message': "Nom d'utilisateur :",
                'default' : str(computer["user"]['username'])
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
                'validate': lambda val: self._checkSelectedIndex(val, 10),
                'default' : str(computer["specs"]['nb_USB_port'])
            }
        ]
        nbStorage = [
            {
                'type': 'input',
                'name': 'nb_storage',
                'message': "Combien d'espaces de stockage l'ordinateur a t'il ? :",
                'validate': lambda val: self._checkSelectedIndex(val, 10),
                'default' : str(len(computer["specs"]['storage']))
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
                    'validate': lambda val: self._checkSelectedIndex(val, 10),
                    'default' : str(computer['specs']['storage'][i]['port']) if len(computer['specs']['storage']) > i else ""
                },
                {
                    'type': 'input',
                    'name': 'type',
                    'message': 'Type :',
                    'default' : str(computer['specs']['storage'][i]['type']) if len(computer['specs']['storage']) > i else ""
                },
                {
                    'type': 'input',
                    'name': 'size',
                    'message': 'Taille :',
                    'default' : str(computer['specs']['storage'][i]['size']) if len(computer['specs']['storage']) > i else ""
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


