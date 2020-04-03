import npyscreen
from api import API
import curses

class SearchTextField(npyscreen.Textfield):
    def __init__(self, *args, **keywords):
        super(SearchTextField, self).__init__(*args, **keywords)
        self.editable = True
        self.add_handlers({
            curses.ascii.NL: self.__search
        })
        
    def __search(self, charCode):
        RoomsForm.updateSearchResults(RoomsForm.api.searchRooms(self.value))

class SearchBar(npyscreen.BoxTitle):
    _contained_widget = SearchTextField
    
class ButtonAddRoom(npyscreen.ButtonPress):
    def __init__(self, *args, **keywords):
        super(ButtonAddRoom, self).__init__(*args, **keywords)
        self.name="+ Salle"

    def whenPressed(self):
        self.find_parent_app().switchForm("ADD_ROOM")
        
class ButtonAddRoomBox(npyscreen.BoxTitle):
    _contained_widget = ButtonAddRoom

class MultiAction(npyscreen.MultiLineAction):
    def __init__(self, *args, **keywords):
        super(MultiAction, self).__init__(*args, **keywords)

    def  actionHighlighted(self, act_on_this, key_press):
        if key_press == curses.ascii.NL:
            self.find_parent_app().switchForm("SOFTWARES")
        elif key_press == curses.ascii.SP:
            # On récupère l'id de la room à partir de l'index de la liste dans le tableau affiché et 
            # notre tableau de données
            room_id = list(RoomsForm.searchResultsData.keys())[self.values.index(act_on_this)]
            if npyscreen.notify_ok_cancel("Est ce que vous êtes sur de supprimer cette salle ?", "Confirmation"):
                if RoomsForm.api.removeRoom(room_id):
                    npyscreen.notify_confirm("La salle " + RoomsForm.searchResultsData[room_id]["room_name"] + " à bien été supprimée", "Succès")
                    del RoomsForm.searchResultsData[room_id]
                    RoomsForm.updateSearchResults(RoomsForm.searchResultsData)
                else:
                    npyscreen.notify_confirm("Une erreur est apparue lors de la suppression de la salle", "Erreur")

class MultiActionBox(npyscreen.BoxTitle):
    _contained_widget = MultiAction
    
class RoomsForm(npyscreen.ActionFormMinimal):
    searchResults = None
    api = API()
    searchResultsData = {}

    @staticmethod
    def updateSearchResults(values):
        RoomsForm.searchResultsData = values
        RoomsForm.searchResults.values = []
        for key in values.keys():
            RoomsForm.searchResults.values.append("⌂  " + values[key]["building_name"] + "\t --> \t" + values[key]["room_name"] + "\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t [Suppr] : Supprimer, \t\t\t\t[↵] : Accéder à la salle")
        RoomsForm.searchResults.update()
        
    def create(self):
        self.build()

    def build(self):
        self.add(SearchBar, name="Rechercher une salle : ", 
            max_height=4,
            max_width=50,
            relx=15,
            rely=1,
        )
        self.add(ButtonAddRoomBox,
            max_height=3,
            max_width=15,
            relx=70,
            rely=2,
        )
        RoomsForm.searchResults = self.add(MultiActionBox, 
            editable=True,
            values=[],
            name="Salles : ",
            scroll_exit=True
        )

    def on_ok(self):
        self.find_parent_app().switchForm("MAIN")
