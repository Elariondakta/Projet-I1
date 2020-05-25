from PyInquirer import prompt, Separator
from prettytable import PrettyTable
from utils import clear
from api import API
from datetime import datetime
import style

class Computers :

    def __init__(self, computer_id = False): ##Métthode qui charge les données etc...
        self.base_data = API.getComputers()
        self.active_data = API.getComputers()      
        self.computer_id = computer_id  

    def display(self):  ##Méthode qui lance l'affichage avec interaction etc...
        clear()

        if not self.computer_id:
            self.display_options()
        else:
            self.display_computer_detail(self.computer_id)

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
                    "Lister les ordinateurs",
                    "Lister les détails d'un ordinateur",
                    "Effectuer une recherche",
                    Separator(),
                    "Retour"
                ]
            }
        ]

        try:
            res = prompt(options)["action_choices"]
            res_index = options[0]['choices'].index(res)
            if res_index == 0:
                ##On ajoute un ordi
                self.addComputer ()
            elif res_index == 1:
                ##On supprime un ordi
                self.remove_computer_display()
                pass
            elif res_index == 2:
                ##On liste les ordis 
                self.display_tables()
                self.display_options()
                pass
            elif res_index == 3:
                ##On liste les détails d'un ordi
                computer_id = self.form_get_id_computer()            
                self.display_computer_detail(computer_id)

            elif res_index == 4:
                ##On effectue une recherche 
                self.display_search()
                self.display_options()
                pass
            elif res_index == 6:
                pass
        except:
            self.display()

    def display_search(self): ##Formulaire de recherche de salle
        options = [
            {
                'type': 'input',
                'name': 'search_query',
                'message': 'Rechercher un ordinateur par nom : ',
            },
        ]
        query = prompt(options)["search_query"]
        self.active_data = API.searchComputers(query)
        self.display_tables(True)

    def addComputer (self):

        name = [
            {
                'type': 'input',
                'name': 'name',
                'message': "Nom de l'ordinateur",
                'validate': lambda val: True if val != "" else "Nom invalide"
            },
        ]

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

        nameData = prompt(name)["name"]
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

        clear()
        if confirmData: 
            API.addComputer(nameData, processorData, RAMData, graphic_cardData, video_portsData, screenData, network_cardData, purchaseData, userData, specs_techData, USBData, storageData, "")
            print(style.green("L'ordinateur a bien été ajouté !"))
        else:
            print(style.red("Action annulée"))

        self.display_options()
        



    def form_get_id_computer(self):
        options = [
            {
                'type': 'input',
                "message": "Entrez L'identifiant de l'ordinateur",
                "name": 'computer_id',
                "validate": lambda val: self._checkSelectedIndex(val, len(self.base_data))
            }
        ]
        index = int(prompt(options)["computer_id"])
        id = list(API.getComputers().keys())[index]

        return id

    def remove_computer_display(self):

        computer_id = self.form_get_id_computer()
        
        confirm = [
            {
                'type': 'confirm',
                'name': "confirm",
                'message': "Etes-vous sur de supprimer l'ordinateur de " + API.getComputers()[computer_id]["user"]["name"] +" ?"
            }
        ]
        res = prompt(confirm)["confirm"]

        clear()

        if res == True:
            API.removeComputer(computer_id)
            print(style.green("L'ordinateur a bien été supprimé !"))
        else :
            print(style.red("Action annulée"))

        self.display_options()

    def display_tables(self, disp_active = False):
        table = PrettyTable()
        table.field_names = ["Id", "Nom", "Utilisateur", "Logiciels", "Salle", "Bâtiment"]
        i = 0
        for table_row_key in self.base_data.keys():         #Pour chaque ordinateur de la base de donnée
            if table_row_key not in list(self.active_data.keys()) and disp_active:  #Si on a active le mode recherche et si l'ordinateur ne se
                i += 1  #trouve pas dans les résulats de recherche on affiche rien mais on incrément de un pour garder un id cohérent
                continue
            else:
                table_row_el = self.base_data[table_row_key]  #Sinon on affiche les données

                table.add_row([
                    i, 
                    table_row_el["name"],
                    table_row_el["user"]["username"], 
                    str(len(table_row_el["softwares"])) + " logiciel(s) installé(s)",
                    "Pas de salle attribuée" if API.getRoom(table_row_el["localisation"]) == None else API.getRoom(table_row_el["localisation"])["room_name"],
                    "Pas de salle attribuée" if API.getRoom(table_row_el["localisation"]) == None else API.getRoom(table_row_el["localisation"])["building_name"]
                ])
                i += 1
        print(table)
        

    def display_computer_detail(self, computer_id):      
    
        computer = API.getComputer(computer_id) ##Demander l'id de l'ordi à l'utilisateur
        
        clear()
        
        print("Ordinateur : " + str(computer['name']) + "\n")
        print(Separator())
        print(style.bold("\nSpécifications techniques :"))

        #Computer
        print(style.blue("\nProcesseur :"))
        print(style.light_cyan("\t" + "Architecture : ") + str(computer["specs"]["processor"]["plateform"]) + " bits")
        print(style.light_cyan("\t" + "Marque : ") + str(computer["specs"]["processor"]["brand"]))
        print(style.light_cyan("\t" + "Vitesse : ") + str(computer["specs"]["processor"]["speed"]))
        print(style.light_cyan("\t" + "Cache : ") + str(computer["specs"]["processor"]["size_cache"]))
        print(style.light_cyan("\t" + "Modèle : ") + str(computer["specs"]["processor"]["model"]))

        #RAM
        print(style.blue("\nRAM :"))
        print(style.light_cyan("\t" + "Nombre de barette : ") + str(computer["specs"]["RAM"]["number"]))
        print(style.light_cyan("\t" + "Taille : ") + str(computer["specs"]["RAM"]["total_size"]))

        #Graphic card
        print(style.blue("\nCarte graphique :"))
        print(style.light_cyan("\t" + "Marque : ") + str(computer["specs"]["graphic_card"]["brand"]))
        print(style.light_cyan("\t" + "Mémoire : ") + str(computer["specs"]["graphic_card"]["memory"]))
        print(style.light_cyan("\t" + "Modèle : ") + str(computer["specs"]["graphic_card"]["model"]))

        #Video port
        print(style.blue("\nPorts vidéo :"))
        print(style.light_cyan("\t" + "Ports vidéo : ") + ', '.join(computer["specs"]["video_port"]))

        #Screen
        print(style.blue("\nEcran :"))
        print(style.light_cyan("\t" + "Résolution : ") + str(computer["specs"]["screen"]['screen_res']))
        print(style.light_cyan("\t" + "Taille : ") + str(computer["specs"]["screen"]['screen_size']).strip('[]').replace(', ', 'x') + "px")

        #Connectors
        print(style.blue("\nConnectique :"))
        print(style.light_cyan("\t" + "Lecteur CD : ") + ("Oui" if  computer["specs"]["CD_player"] else "Non" ))
        print(style.light_cyan("\t" + "Ports USB : ") + str(computer["specs"]["nb_USB_port"]))

        #Stockage
        print(style.blue("\nStockage :"))

        n_storage = 1
        for storage in computer["specs"]['storage']:
            print(style.light_cyan("\tStockage " + str(n_storage) + " :"))
            print(style.magenta("\t\tType : ") + str(storage["type"]))
            print(style.magenta("\t\tPort : ") + str(storage["port"]))
            print(style.magenta("\t\tTaille : ") + str(storage["size"]))
            n_storage+=1

        #Network card
        print(style.blue("\nCarte réseau :"))
        print(style.light_cyan("\t" + "Vitesse : ") + str(computer["specs"]["network_card"]['speed']))
        print(style.light_cyan("\t" + "Marque : ") + str(computer["specs"]["network_card"]['brand']))

        #User
        print(style.blue("\nUtilisateur :"))
        print(style.light_cyan("\t" + "Nom : ") + str(computer["user"]['name']))
        print(style.light_cyan("\t" + "Nom  d'utilisation : ") + str(computer["user"]['username']))

        #Other
        print(style.blue("\nAutre :"))
        print(style.light_cyan("\t" + "WiFi : ") + ("Oui" if  computer["specs"]["wifi"] else "Non" ))
        print(style.light_cyan("\t" + "Bluetooth : ") + ("Oui" if  computer["specs"]["bluetooth"] else "Non" ))
        print(style.light_cyan("\t" + "Fabriquant : ") + str(computer["specs"]["maker"]))
        print(style.light_cyan("\t" + "Fournisseur : ") + str(computer["specs"]["provider"]))
        print(style.light_cyan("\t" + "Date d'achat : ") + datetime.fromtimestamp(computer["specs"]["purchase_date_timestamp"]).strftime("%d/%m/%Y"))

        print("\n")
        print(Separator())

        print(style.bold("\nLocalisation :\n"))
        print(style.blue("Salle :"))

        if API.getRoom(computer["localisation"]) != None:
            print(style.light_cyan("\t" + "Nom : ") + API.getRoom(computer["localisation"])["room_name"])
            print(style.light_cyan("\t" + "Batiment : ") + API.getRoom(computer["localisation"])["building_name"])

        print("\n")
        print(Separator())
        print("\n")

        options = [
            {
                'type': 'list',
                'name': 'menu_computer_detail',
                'message': 'Selectionner un des menus avec les flèches du clavier.',
                'choices': [
                    "Editer",
                    "Logiciels installés",
                    "Ajouter une salle à cet ordinateur",
                    Separator(),
                    "Retour"
                ]
            },
        ]

        res = prompt(options) ##On affiche le formulaire

        try:
            res_index = options[0]['choices'].index(res["menu_computer_detail"])


            if res_index == 0: ##Formulaire d'edition de l'ordinateur
                self.edit_computer_detail(computer_id)
            elif res_index == 1: ##Formulaire des logiciels
                clear()
                self.display_installed_software(computer_id)
            elif res_index == 2:
                clear()
                self.display_rooms()
                self.ask_for_room(computer_id)
            elif res_index == 4: ##Retour
                clear()
                if not self.computer_id:
                    self.display_options()
                else:
                    pass
        except:
            self.display_computer_detail(computer_id)

    def display_rooms(self):
        table = PrettyTable()
        table.field_names = ["Id", "Bâtiment", "Salle"]
        i = 0
        for table_row_key in API.getRooms():
            table_row_el = API.getRooms()[table_row_key]
            table.add_row([i, table_row_el["building_name"], table_row_el["room_name"]])
            i += 1
        print(table)

    def ask_for_room(self, computer_id):
        ask_room_index = [
            {
                'type': 'input',
                'name': 'room_index',
                'message': "Id de la salle"
            }
        ]
        room_index = prompt(ask_room_index)["room_index"]
        room_id = list(API.getRooms().keys())[int(room_index)]
        API.setComputerRoom(computer_id, room_id)
        self.display_computer_detail(computer_id)

    def edit_computer_detail(self, computer_id):
        clear()

        computer = API.getComputer(computer_id)

        print(style.bold("\nEdition de l'ordinateur " + computer['name'] + " :\n"))

        name = [
            {
                'type': 'input',
                'name': 'name',
                'message': "Nom de l'ordinateur :",
                'validate': lambda val: True if val != "" else "Nom invalide",
                'default' : str(computer["name"])
            }
        ]

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
                        'name': 'VGA',
                        'checked' : True if 'VGA' in computer["specs"]["video_port"] else False
                    },
                    {
                        'name': 'HDMI',
                        'checked' : True if 'HDMI' in computer["specs"]["video_port"] else False
                    },
                    {
                        'name': 'Display-Port',
                        'checked' : True if 'Display-Port' in computer["specs"]["video_port"] else False
                    },
                    {
                        'name': 'DVI-A',
                        'checked' : True if 'DVI-A' in computer["specs"]["video_port"] else False
                    },
                    {
                        'name': 'DVI-D',
                        'checked' : True if 'DVI-D' in computer["specs"]["video_port"] else False
                    },
                    {
                        'name': 'USB-C',
                        'checked' : True if 'USB-C' in computer["specs"]["video_port"] else False
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
                        'name': 'Lecteur CD',
                        'checked' : True if computer["specs"]["CD_player"] else False
                    },
                    {
                        'name': 'Wifi',
                        'checked' : True if computer["specs"]["wifi"] else False
                    },
                    {
                        'name': 'Bluetooth',
                        'checked' : True if computer["specs"]["bluetooth"] else False
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

        nameData = prompt(name)["name"]
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
                'message': "Confirmer l'édition de l'ordinateur"
            }
        ]
        confirmData = prompt(confirm)

        if confirmData: 
            new_computer = {
                "name" : nameData,
                "softwares": [],
                "specs": {
                    "processor": processorData,
                    "RAM": RAMData,
                    "graphic_card": graphic_cardData,
                    "video_port": video_portsData,
                    "screen": {
                        "screen_res": screenData["screen_res"],
                        "screen_size": [
                            screenData["screen_size_x"],
                            screenData["screen_size_y"]
                        ]
                    },
                    "nb_USB_port": USBData,
                    "storage": storageData,
                    "network_card": network_cardData,
                    "CD_player": "Lecteur CD" in specs_techData["specs_tech"],
                    "wifi": "Wifi" in specs_techData["specs_tech"],
                    "bluetooth": "Bluetooth" in specs_techData["specs_tech"],
                    "maker": purchaseData["maker"],
                    "provider": purchaseData["provider"],
                    "purchase_date_timestamp": purchaseData["purchase_date_timestamp"]
                },
                "user": userData,
                "localisation": computer["localisation"]
            }
            API.setComputer(computer_id, new_computer)
        
        self.display_computer_detail(computer_id)


    def display_installed_software(self, computer_id):       
        computer = API.getComputer(computer_id)
        clear()
        print(style.bold("\nListe des logiciels installés sur l'ordinateur " + computer['name'] + " :\n"))


        count = 0
        for software in computer['softwares']:
            print(API.getSoftware(software)['name'])

        print("\n")
        print(Separator())
        print("\n")

        options = [
            {
                'type': 'list',
                'name': 'menu_software_detail',
                'message': 'Selectionner un des menus avec les flèches du clavier.',
                'choices': [
                    'Editer les logiciels installés',
                    Separator(),
                    "Retour"
                ]
            },
        ]

        res = prompt(options) ##On affiche le formulaire

        try:
            res_index = options[0]['choices'].index(res["menu_software_detail"])


            if res_index == 0: ##Formulaire d'edition de l'ordinateur
                self.edit_software_in_computer(computer_id)
                
            elif res_index == 2: ##Retour
                clear()
                self.display_computer_detail(computer_id)
        except:
            self.display_installed_software(computer_id)

    def edit_software_in_computer(self, computer_id):
        computer = API.getComputer(computer_id)

        listSoftwares = []
        i = 0
        for software_key in API.getSoftwares():
            listSoftwares.append(
                {
                'name' : " " + str(i) + " : " + API.getSoftware(software_key)["name"], 
                'checked' : True if software_key in computer['softwares'] else False
                }
            )
            i += 1

        new_softwares = [
            {
                'type': 'checkbox',
                'message': 'Selectionner les logiciels',
                'name': 'edit_softwares',
                'choices': listSoftwares
            }
        ]

        listSoftwaresChecked = prompt(new_softwares)['edit_softwares']
        listSoftwareId = []

        for software_req in listSoftwaresChecked:
            index = str(software_req).split(" ")[1] #On récupère l'id affiché dans les questions pour s'en servir d'identifiant
            key = list(API.getSoftwares().keys())[int(index)]
            listSoftwareId.append(key)
        
        API.setSoftwareComputer(computer_id, listSoftwareId)

        clear()

        print(style.green("La liste des logiciels installés sur cet ordinateur a bien été mise à jour !"))

        self.display_installed_software(computer_id)
        



