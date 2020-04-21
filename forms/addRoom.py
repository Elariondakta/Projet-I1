import npyscreen
import curses
from api import API
from forms.rooms import RoomsForm
class AddRoom(npyscreen.ActionFormV2):
    def create(self):
        self.buildingField = self.add(npyscreen.TitleText, name="Batiment : ", relx=10)
        self.nextrely += 1
        self.roomField = self.add(npyscreen.TitleText, name="Salle : ", relx=10)


    def on_ok(self):
        if len(self.roomField.get_value()) == 0 or len(self.buildingField.get_value()) == 0:
            npyscreen.notify_confirm("Vous devez remplir tous les champs du formulaires avant de confirmer", "Erreur")
            return;
        
        if API.addRoom(self.roomField.get_value(), self.buildingField.get_value()):
            npyscreen.notify_confirm("La salle " + self.roomField.get_value() + " à bien été ajoutée", "Succès")
            RoomsForm.updateSearchResults(API.searchRooms(""))  #On réinitialise les donnée affichée pour que notre ajout soit affiché
            self.find_parent_app().switchForm("ROOMS")
        else:
            npyscreen.notify_confirm("Une erreur est apparue lors de l'ajout de votre salle", "Erreur")

    def on_cancel(self):
        self.find_parent_app().switchForm("ROOMS")