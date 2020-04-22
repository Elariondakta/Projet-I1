import npyscreen
from api import API
import curses
from utils import *
    
class ViewRoom(npyscreen.ActionFormMinimal):
    isCreated = False
        
    def create(self):
        pass

    def build(self):
        if transfertArgs.args['room_id'] == "" or ViewRoom.isCreated:
            return

        self.roomField = self.add(npyscreen.FixedText, name="Salle", value = "Salle : " + API.getRoom(transfertArgs.args['room_id'])['room_name'], relx=10, )
        self.roomField = self.add(npyscreen.FixedText, name="Batiment", value="Batiment : " + API.getRoom(transfertArgs.args['room_id'])['building_name'], relx=10, )

    def while_editing(self, *args, **keywords):

        self.build()
        ViewRoom.isCreated = True
        return super().while_editing(*args, **keywords)

    
        

