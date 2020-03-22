import npyscreen
from api import API
import curses

class SearchTextField(npyscreen.Textfield):
    def __init__(self, *args, **keywords):
        super(SearchTextField, self).__init__(*args, **keywords)
        self.editable = True
        self.add_handlers({
            " ": self.__search
        })
        
    def __search(self, charCode):
        RoomsForm.updateSearchResults(RoomsForm.api.searchRooms(self.value))

class SearchBar(npyscreen.BoxTitle):
    _contained_widget = SearchTextField
    
class ButtonAddRoom(npyscreen.ButtonPress):
    def __init__(self, *args, **keywords):
        super(ButtonAddRoom, self).__init__(*args, **keywords)
        self.name="+ Salle"
        
class ButtonAddRoomBox(npyscreen.BoxTitle):
    _contained_widget = ButtonAddRoom
    
class RoomsForm(npyscreen.Form):
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
        RoomsForm.searchResults = self.add(npyscreen.MultiLineEditableBoxed, 
            editable=True,
            values=[],
            name="Salles : "
        )
