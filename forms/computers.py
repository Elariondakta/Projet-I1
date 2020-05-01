from PyInquirer import prompt
from prettytable import PrettyTable
from utils import clear
from api import API
class Computers :
    def __init__(self): ##Métthode qui charge les données etc...
        pass

    def display(self):  ##Méthode qui lance l'affichage avec interaction etc...
        clear()

    def _checkSelectedIndex(self, val):
        try:
            if int(val) > 0 and int(val) < 10:
                return True
            else: return "Vous devez rentrer un nombre entre 0 et 10."
        except:
            return "Vous devez rentrer un nombre."

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
            pass
        elif res_index == 1:
            ##On supprime un ordi
            pass
        elif res_index == 2:
            ##On renomme un ordi
            pass
        elif res_index == 3:
            ##On liste les ordis 
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
                'message': 'Platform :',
            },
            {
                'type': 'input',
                'name': 'brand',
                'message': 'Brand :',
            },
            {
                'type': 'input',
                'name': 'speed',
                'message': 'Speed :',
            },
            {
                'type': 'input',
                'name': 'size_cache',
                'message': 'Cache Size :',
            },
            {
                'type': 'input',
                'name': 'model',
                'message': 'Model :',
            }
        ]
        RAM = [
            {
                'type': 'input',
                'name': 'number',
                'message': 'Number of RAM :',
            },
            {
                'type': 'input',
                'name': 'total_size',
                'message': 'Total Size :',
            }
        ]
        graphic_card = [
            {
                'type': 'input',
                'name': 'brand',
                'message': 'Brand :',
            },
            {
                'type': 'input',
                'name': 'memory',
                'message': 'Memory Size :',
            },
            {
                'type': 'input',
                'name': 'model',
                'message': 'Card Model :',
            }
        ]
        video_ports = [
            {
                'type': 'checkbox',
                'message': 'Select ports (To select, press space)',
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
                'message': 'Screen Resolution :',
            },
            {
                'type': 'input',
                'name': 'screen_size_x',
                'message': 'Screen Width :',
            },
            {
                'type': 'input',
                'name': 'screen_size_y',
                'message': 'Screen Height :',
            }
        ]
        network_card = [
            {
                'type': 'input',
                'name': 'speed',
                'message': 'Speed :',
            },
            {
                'type': 'input',
                'name': 'brand',
                'message': 'Brand :',
            }
        ]
        purchase = [
            {
                'type': 'input',
                'name': 'maker',
                'message': 'Maker :',
            },
            {
                'type': 'input',
                'name': 'provider',
                'message': 'Provider :',
            },
            {
                'type': 'input',
                'name': 'purchase_date_timestamp',
                'message': 'Purchase Date Timestamp :',
            }
        ]
        user = [
            {
                'type': 'input',
                'name': 'name',
                'message': 'Name :',
            },
            {
                'type': 'input',
                'name': 'username',
                'message': 'Username :',
            },
            {
                'type': 'input',
                'name': 'ID',
                'message': 'ID :',
            }
        ]
        specs_tech = [
            {
                'type': 'checkbox',
                'message': 'Select technical caracteristics (To select, press space)',
                'name': 'specs_tech',
                'choices': [ 
                    {
                        'name': 'CD Player'
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
                'message': 'How many USB ports does the computer have ? :',
                'validate': lambda val: self._checkSelectedIndex(val)
            }
        ]
        nbStrorage = [
            {
                'type': 'input',
                'name': 'nb_storage',
                'message': "Combien d'espaces de stockage l'ordinateur a t'il ? :",
                'validate': lambda val: self._checkSelectedIndex(val)
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
        nbStrorageData = int(prompt(nbStrorage)["nb_storage"])
        
        storageData = []

        for i in range(0, nbStrorageData):
            storageData.append(prompt([
                {
                    'type': 'input',
                    'name': 'type',
                    'message': 'Type :',
                },
                {
                    'type': 'input',
                    'name': 'size',
                    'message': 'Size :',
                }
            ]))
        
