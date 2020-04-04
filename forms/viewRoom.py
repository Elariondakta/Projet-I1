import npyscreen
from api import API
import curses
from utils import *
    
class ViewRoom(npyscreen.ActionFormMinimal):
    api = API()
        
    def create(self):
        self.build()

    def build(self):
        print(transfertArgs.args['room_id'])
        

