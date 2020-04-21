import npyscreen
from api import API
from utils import TransfertArgs
import curses

class SearchTextField(npyscreen.Textfield):
    def __init__(self, *args, **keywords):
        super(SearchTextField, self).__init__(*args, **keywords)
        self.editable = True
        self.add_handlers({
            curses.ascii.NL: self.__search
        })
        
    def __search(self, charCode):
        RoomsForm.updateSearchResults(API.searchRooms(self.value))

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

    def actionHighlighted(self, act_on_this, key_press):
        print(key_press)
        room_id = list(RoomsForm.searchResultsData.keys())[self.values.index(act_on_this)]
        if key_press == curses.ascii.NL:
            TransfertArgs.args = {"room_id" : room_id}
            self.find_parent_app().switchForm("VIEW_ROOM")
        if key_press == curses.ascii.SP:   #SP
            # On récupère l'id de la room à partir de l'index de la liste dans le tableau affiché et 
            # notre tableau de données           
            if npyscreen.notify_ok_cancel("Est ce que vous êtes sur de supprimer cette salle ?", "Confirmation"):
                if API.removeRoom(room_id):
                    npyscreen.notify_confirm("La salle " + RoomsForm.searchResultsData[room_id]["room_name"] + " à bien été supprimée", "Succès")
                    RoomsForm.updateSearchResults(API.searchRooms(""))  #On réinitialise les donnée affichée pour que notre ajout soit affiché
                else:
                    npyscreen.notify_confirm("Une erreur est apparue lors de la suppression de la salle", "Erreur")

class MultiActionBox(npyscreen.BoxTitle):
    _contained_widget = MultiAction
    
class RoomsForm(npyscreen.ActionFormMinimal):
    searchResults = None
    searchResultsData = {}

    @staticmethod
    def updateSearchResults(values):
        RoomsForm.searchResultsData = values
        RoomsForm.searchResults.values = []
        for key in values.keys():
            RoomsForm.searchResults.values.append("⌂  " + values[key]["building_name"] + "\t --> \t" + values[key]["room_name"] + "\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t [Espace] : Supprimer, \t\t\t\t[↵] : Accéder à la salle")
        RoomsForm.searchResults.update()
        
    def create(self):
        self.build()
        RoomsForm.updateSearchResults(API.searchRooms(""))

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
