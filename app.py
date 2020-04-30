from npyscreen import NPSAppManaged
from forms.home import HomeForm
from forms.breach import BreachForm
from forms.computers import ComputersForm
from forms.software import SoftwareForm
from forms.rooms import RoomsForm
from forms.addRoom import AddRoom
from forms.viewRoom import ViewRoom
from forms.viewComputer import ViewComputer
from api import API
from const import *

class App(NPSAppManaged):
    def onStart(self):
        self.registerForm("MAIN", HomeForm(name="Gestionnaire de ressources matérielles (V1.0):"))
        self.registerForm("COMPUTERS", ComputersForm(name="Vue des ordinateurs"))
        self.registerForm("BREACH", BreachForm(name="Vulnérabilitées"))
        self.registerForm("SOFTWARES", SoftwareForm(name="Vue des logiciels"))
        self.registerForm("ROOMS", RoomsForm(name="Vue des salles"))
        self.registerForm("ADD_ROOM", AddRoom(name="Ajout d'une salle"))
        self.registerForm("VIEW_ROOM", ViewRoom(name="Salle"))
        self.registerForm("VIEW_COMPUTER", ViewComputer(name="Vue d'un ordinateur"))

