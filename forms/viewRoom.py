import npyscreen
from api import API
import curses

    
class ViewRoom(npyscreen.ActionFormMinimal):
    api = API()
        
    def create(self):
        self.build()

    def build(self):
        print("ok")

