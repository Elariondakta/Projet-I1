import npyscreen
import curses
from api import API

#hiskfsdzzdzz
#ssjdsjdsdsj
#"software": {
#            "name": "OpenOffice",
#            "editor": "Francis",
#            "provider": "Microsoft",
#            "version": "2.4.3892",
#            "licence_exp_date": 3456787456,
#            "ID": "trhdfg3356",
#            "add_on": {
#                "ID": "trhdfg3356",
#                "name": "OpenOffice",
#                "editor": "Francis",
#                "provider": "Microsoft",
#                "version": "2.4.3892"

class addAddOn(npyscreen.ActionFormV2):      
    def create(self):
        self.IDField = self.add(npyscreen.TitleText, name="Identifiant : ", relx=10)
        self.nextrely += 1
        self.nameField = self.add(npyscreen.TitleText, name="Nom : ", relx=10)
        self.nextrely += 1
        self.editorField = self.add(npyscreen.TitleText, name="Editor : ", relx=10)
        self.nextrely += 1
        self.providorField = self.add(npyscreen.TitleText, name="Fournisseur : ", relx=10)
        self.nextrely += 1
        self.versionField = self.add(npyscreen.TitleText, name="Version : ", relx=10)

    
    def on_ok(self):
        if len(self.editorField.get_value()) == 0 or len(self.nameField.get_value()) == 0 or len(self.providorField.get_value()) == 0 or len(self.versionField.get_value()) == 0 or len(self.IDField.get_value()) == 0:
            npyscreen.notify_confirm("Vous devez remplir tous les champs du formulaires avant de confirmer", "Erreur")
            return;
        
        if API.addRoom(self.nameField.get_value(), self.nameField.get_value()):
            npyscreen.notify_confirm("Le plug in " + self.nameField.get_value() + " à bien été ajoutée", "Succès")
            # RoomsForm.updateSearchResults(API.searchRooms(""))  #On réinitialise les donnée affichée pour que notre ajout soit affiché
            self.find_parent_app().switchForm("MAIN") #A MODIFIER ET REMPLACER PAR "ADD_SOFTWARE" quand on ne lancera plus plus que ca !!
        else:
            npyscreen.notify_confirm("Une erreur est apparue lors de l'ajout de votre salle", "Erreur")

    def on_cancel(self):
        self.find_parent_app().switchForm("ADD_SOFTWARE")