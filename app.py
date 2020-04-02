from npyscreen import NPSAppManaged
from forms.home import HomeForm
from forms.breach import BreachForm
from forms.computers import ComputersForm
from forms.software import SoftwareForm
from forms.rooms import RoomsForm
from forms.addRoom import AddRoom
from const import *

class App(NPSAppManaged):
    def onStart(self):
        # self.registerForm("MAIN", HomeForm(name="Gestionnaire de ressources matérielles (V1.0):"))
        self.registerForm("COMPUTERS", ComputersForm(name="Vue des ordinateurs"))
        self.registerForm("BREACH", BreachForm(name="Vulnérabilitées"))
        self.registerForm("SOFTWARES", SoftwareForm(name="Vue des logiciels"))
        self.registerForm("ROOMS", RoomsForm(name="Vue des salles"))
        self.registerForm("MAIN", AddRoom(name="Ajout d'une salle"))