import npyscreen
from api import API
import curses
from utils import *


class MultiAction(npyscreen.MultiLineAction):
    def __init__(self, *args, **keywords):
        super(MultiAction, self).__init__(*args, **keywords)

    def actionHighlighted(self, act_on_this, key_press):
        computer_index = self.values.index(act_on_this)
        computer = ""

        for computer in API.getComputersInRoom(transfertArgs.args['room_id']):
            if act_on_this == "⌂  " + computer + "\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t[↵] : Détails":
                computer_id = computer
                break
        
        if computer_id == "":
            return;
     
        if key_press == curses.ascii.NL:
            transfertArgs.args = {"computer_id" : computer_id}
            self.find_parent_app().switchForm("VIEW_COMPUTER")

class MultiActionBox(npyscreen.BoxTitle):
    _contained_widget = MultiAction   
class ViewRoom(npyscreen.ActionFormMinimal):

    isCreated = False
    computersList = []
    computerIndexList = []
    
        
    def create(self):
        pass

    def build(self):
        if transfertArgs.args['room_id'] == "" or ViewRoom.isCreated:
            return

        self._clear_all_widgets()
        self.create_control_buttons()

        self.roomField = self.add(npyscreen.FixedText, name="Salle", value = "Salle : " + API.getRoom(transfertArgs.args['room_id'])['room_name'], relx=10, )
        self.roomField = self.add(npyscreen.FixedText, name="Batiment", value="Batiment : " + API.getRoom(transfertArgs.args['room_id'])['building_name'], relx=10, )

        computersList = []
        computerIndexList = []
        for computer in API.getComputersInRoom(transfertArgs.args['room_id']):
            computersList.append("⌂  " + computer + "\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t[↵] : Détails")
            computerIndexList.append(computer)


        self.searchResults = self.add(MultiActionBox, 
            editable=True,
            values=computersList,
            name="Liste des ordinateurs présents dans la salle :",
            scroll_exit=True
        )

        self.searchResults.update()


    def while_editing(self, *args, **keywords):

        self.build()
        ViewRoom.isCreated = True
        return super().while_editing(*args, **keywords)

    def on_ok(self):
        ViewRoom.isCreated = False   
         
        self.find_parent_app().switchForm("ROOMS")
        

    
        

